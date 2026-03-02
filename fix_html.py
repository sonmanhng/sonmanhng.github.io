import re
import glob

# Files to process
html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Check if canvas already exists to avoid duplicates
    if '<canvas id="bg-canvas"></canvas>' not in content:
        # Match <body ...> and append canvas after it
        content = re.sub(
            r'(<body[^>]*>)',
            r'\1\n    <canvas id="bg-canvas"></canvas>',
            content,
            count=1 # Only replace the first opening body tag
        )
        
        with open(file, 'w') as f:
            f.write(content)
            print(f"Fixed {file}")
    else:
        print(f"Canvas already exists in {file}")

