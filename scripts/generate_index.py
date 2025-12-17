import os
import json
import datetime
import shutil

def generate_index():
    dist_dir = './dist'
    
    # Ensure dist exists
    if not os.path.exists(dist_dir):
        print(f"Directory {dist_dir} does not exist.")
        return

    # Copy template
    template_path = 'resources/index.html'
    if os.path.exists(template_path):
        shutil.copy(template_path, os.path.join(dist_dir, 'index.html'))
        print("Copied index.html template.")
    else:
        print(f"Template {template_path} not found.")

    repo = os.environ.get('GITHUB_REPOSITORY')
    if repo:
        user, repo_name = repo.split('/')
        if repo_name == f"{user}.github.io":
            base_url = f"https://{repo_name}/"
        else:
            base_url = f"https://{user}.github.io/{repo_name}/"
    else:
        base_url = ""

    files = []
    for f in os.listdir(dist_dir):
        if f.endswith('.pdf'):
            path = os.path.join(dist_dir, f)
            stat = os.stat(path)
            # filename is like 'backend-resume.pdf', extract 'backend'
            profile_key = f.replace('-resume.pdf', '').lower()
            profile = profile_key.capitalize()
            
            # If capitalization fails or structure is different, fallback
            if profile == f:
                profile = "Unknown"
                profile_key = "unknown"

            # Attempt to read description from profile source
            description = ""
            profile_tex = os.path.join('profiles', f'{profile_key}.tex')
            if os.path.exists(profile_tex):
                try:
                    with open(profile_tex, 'r') as pf:
                        first_line = pf.readline().strip()
                        if first_line.startswith('%'):
                            description = first_line.lstrip('%').strip()
                except Exception as e:
                    print(f"Error reading description for {profile_key}: {e}")
            
            files.append({
                'name': f,
                'profile': profile,
                'description': description,
                'url': f"{base_url}{f}",
                'size': stat.st_size,
                'date': datetime.datetime.fromtimestamp(stat.st_mtime).isoformat()
            })

    data = {
        'metadata': {
            'generated_at': datetime.datetime.now().isoformat()
        },
        'files': sorted(files, key=lambda x: x['profile'])
    }
    
    json_path = os.path.join(dist_dir, 'resumes.json')
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Generated resumes.json with {len(files)} files.")

if __name__ == "__main__":
    generate_index()
