import os
import re
import argparse
from pathlib import Path

# Map old paths to new paths
# Since \input paths don't have .tex usually, we map without extension.
# We also map with .tex just in case.

def build_path_map():
    # Build a mapping from old file path (relative to repo root) to new file path
    # We can inspect the git status to find renames.
    path_map = {}
    import subprocess
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if line.startswith('R  ') or line.startswith('RM '):
            parts = line[3:].split(' -> ')
            if len(parts) == 2:
                old_path = parts[0].strip()
                new_path = parts[1].strip()

                # remove .tex extension
                old_no_ext = old_path[:-4] if old_path.endswith('.tex') else old_path
                new_no_ext = new_path[:-4] if new_path.endswith('.tex') else new_path

                path_map[old_no_ext] = new_no_ext
                path_map[old_path] = new_path

    return path_map

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Print changes without modifying files')
    args = parser.parse_args()

    path_map = build_path_map()

    # We also need to map things like 'preamble' to 'config/preambles/cv_preamble'
    # Wait, 'preamble' -> 'config/preambles/cv_preamble'
    # 'resume_preamble' -> 'config/preambles/resume_preamble'
    # 'macros' -> 'config/macros/shared_macros'
    # 'resume_macros' -> 'config/macros/resume_macros'

    path_map['preamble'] = 'config/preambles/cv_preamble'
    path_map['resume_preamble'] = 'config/preambles/resume_preamble'
    path_map['macros'] = 'config/macros/shared_macros'
    path_map['resume_macros'] = 'config/macros/resume_macros'


    # Let's walk through all .tex files in the repo
    repo_root = Path('.')
    tex_files = list(repo_root.rglob('*.tex'))

    input_pattern = re.compile(r'\\input\{([^}]+)\}')

    for file_path in tex_files:
        # Ignore things in output or .git
        if 'output' in file_path.parts or '.git' in file_path.parts:
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        def repl(match):
            input_path = match.group(1)

            # Remove any trailing .tex if present to standardize mapping
            lookup_path = input_path

            # Some paths might have \currentprofile, which makes it dynamic
            # In the original, they were sections/experience/\currentprofile_experience_resume
            # We already fixed main_resume.tex and the entry files, so we might not need to touch \currentprofile
            # if it's not present. But let's check if it's in our map.
            if '\\currentprofile' in lookup_path:
                 return match.group(0) # Keep as is, or we might need to handle it. Actually, we removed main_resume.tex's \currentprofile usage by creating thin files.

            if lookup_path in path_map:
                new_target = path_map[lookup_path]

                # Compute relative path from file_path to new_target
                # For latex \input, it can be relative to the invoking document or relative to the file.
                # Usually it's relative to the invoking document (the root).
                # But since the entry files are now in documents/cv or documents/resume,
                # the \input path in those entry files needs to be relative to the entry file!
                # E.g. inside documents/cv/backend.tex, \input{sections/summary} needs to be \input{../../content/summary_master}

                # Calculate relative path
                file_dir = file_path.parent

                # new_target is relative to repo root.
                # We need the path to new_target relative to file_dir
                target_full = repo_root / new_target

                try:
                    rel_path = os.path.relpath(target_full, file_dir)
                    # Replace \ with / for LaTeX
                    rel_path = rel_path.replace('\\', '/')

                    # Print change
                    if args.dry_run:
                        print(f"[{file_path}] \\input{{{input_path}}} -> \\input{{{rel_path}}}")

                    return f'\\input{{{rel_path}}}'
                except ValueError:
                    return match.group(0)

            # If not in path_map exactly, check if we can resolve it
            # e.g., if input_path is "experience/isa_internship_short" and we moved it to "content/experience/short/isa_internship_short"
            # we need to find where "isa_internship_short" ended up.

            # find by filename
            base_name = os.path.basename(input_path)
            for old, new in path_map.items():
                if os.path.basename(old) == base_name:
                    new_target = new
                    target_full = repo_root / new_target
                    rel_path = os.path.relpath(target_full, file_path.parent).replace('\\', '/')
                    if args.dry_run:
                        print(f"[{file_path}] (fuzzy) \\input{{{input_path}}} -> \\input{{{rel_path}}}")
                    return f'\\input{{{rel_path}}}'

            return match.group(0)

        new_content = input_pattern.sub(repl, content)

        if new_content != content and not args.dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

if __name__ == '__main__':
    main()
