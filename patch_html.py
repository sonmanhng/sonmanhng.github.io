import re
import glob

# Files to process
html_files = glob.glob('*.html')
three_js_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n    <script src="scripts.js"></script>'

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Inject Three.js
    content = re.sub(
        r'<script src="scripts\.js"></script>',
        three_js_script,
        content
    )
    
    with open(file, 'w') as f:
        f.write(content)

with open('styles.css', 'r') as f:
    css_content = f.read()

# Define new light theme colors
css_content = re.sub(r"--bg-color: [^;]+;", "--bg-color: #fafafa;", css_content)
css_content = re.sub(r"--card-bg: [^;]+;", "--card-bg: #ffffff;", css_content)
css_content = re.sub(r"--primary-color: [^;]+;", "--primary-color: #1e293b;", css_content) # Dark slate for text
css_content = re.sub(r"--secondary-color: [^;]+;", "--secondary-color: #64748b;", css_content) # Muted slate
css_content = re.sub(r"--accent-color: [^;]+;", "--accent-color: #0284c7;", css_content) # Quantum light blue
css_content = re.sub(r"--border-color: [^;]+;", "--border-color: rgba(15, 23, 42, 0.1);", css_content) # Dark border with transparency

# Update specific styles for light theme
css_content = re.sub(
    r"body::before \{\n    content: \"\";\n    position: fixed;\n    top: 0;\n    left: 0;\n    width: 100%;\n    height: 100%;\n    background: linear-gradient\(rgba\(18, 16, 16, 0\) 50%,\n            rgba\(0, 0, 0, 0\.1\) 50%\);\n    background-size: 100% 4px;\n    z-index: 9999;\n    pointer-events: none;\n    opacity: 0\.15;\n\}",
    "/* Scanlines removed for light academic theme */",
    css_content
)

css_content = re.sub(
    r"background: rgba\(13, 17, 23, 0\.85\);",
    "background: rgba(255, 255, 255, 0.9);",
    css_content
)

css_content = re.sub(
    r"text-shadow: 0 0 20px rgba\(255, 255, 255, 0\.1\);",
    "text-shadow: none;",
    css_content
)

css_content = re.sub(
    r"color: rgba\(255, 255, 255, 0\.8\);",
    "color: var(--primary-color);",
    css_content
)

css_content = re.sub(
    r"color: rgba\(255, 255, 255, 0\.9\);",
    "color: var(--primary-color);",
    css_content
)

css_content = re.sub(
    r"background: rgba\(255, 255, 255, 0\.02\);",
    "background: #ffffff; box-shadow: 0 2px 5px rgba(0,0,0,0.02);",
    css_content
)

# Darken profile image border
css_content = re.sub(
    r"border-color: rgba\(255, 255, 255, 0\.3\);",
    "border-color: rgba(15, 23, 42, 0.2);",
    css_content
)

css_content = re.sub(
    r"filter: grayscale\(1\) contrast\(1\.1\);",
    "filter: grayscale(0.2) contrast(1.05); /* Softer image for light theme */",
    css_content
)

css_content = re.sub(
    r"\.profile-img:hover \{\n    filter: grayscale\(0\) contrast\(1\);\n    border-color: rgba\(15, 23, 42, 0\.2\);\n\}",
    ".profile-img:hover {\n    filter: grayscale(0) contrast(1);\n    border-color: var(--accent-color);\n    box-shadow: 0 4px 12px rgba(2, 132, 199, 0.15);\n}",
    css_content
)

with open('styles.css', 'w') as f:
    f.write(css_content)
