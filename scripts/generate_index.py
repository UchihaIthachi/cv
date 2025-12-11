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

    files = []
    for f in os.listdir(dist_dir):
        if f.endswith('.pdf'):
            path = os.path.join(dist_dir, f)
            stat = os.stat(path)
            # filename is like 'backend-resume.pdf', extract 'backend'
            profile = f.replace('-resume.pdf', '').capitalize()
            # If capitalization fails or structure is different, fallback
            if profile == f:
                profile = "Unknown"
            
            files.append({
                'name': f,
                'profile': profile,
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
