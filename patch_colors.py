import re

with open('styles.css', 'r') as f:
    content = f.read()

# Replace fonts import
content = re.sub(
    r"@import url\('https://fonts.googleapis.com/css2\?family=Space\+Mono:wght@400;700\&family=Outfit:wght@300;400;500;600;700;800\&display=swap'\);",
    "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300..700&family=Lora:ital,wght@0,400..700;1,400..700&display=swap');",
    content
)

# Colors
content = re.sub(r"--bg-color: #080808;", "--bg-color: #0d1117;", content) # slightly lighter than pure black, github dark mode dim
content = re.sub(r"--card-bg: rgba\(20, 20, 20, 0\.6\);", "--card-bg: rgba(22, 27, 34, 0.6);", content)
content = re.sub(r"--primary-color: #ffffff;", "--primary-color: #f0f6fc;", content)
content = re.sub(r"--secondary-color: #d1d1d1;", "--secondary-color: #8b949e;", content)
content = re.sub(r"--accent-color: #ffffff;", "--accent-color: #58a6ff;", content) # quantum blue
content = re.sub(r"--border-color: rgba\(255, 255, 255, 0\.15\);", "--border-color: rgba(240, 246, 252, 0.1);", content)

# Fonts
content = re.sub(r"--font-heading: 'Inter', sans-serif;", "--font-heading: 'Lora', serif;", content)
content = re.sub(r"--font-body: 'Inter', sans-serif;", "--font-body: 'Inter', sans-serif;", content)
content = re.sub(r"--font-mono: 'Lora', monospace;", "--font-mono: 'Inter', sans-serif;", content) # Use Inter instead of mono for a cleaner look

# Remove HUD Accents
content = re.sub(r"\.sidebar h2::before \{[^}]+\}", "", content)
content = re.sub(r"\.sidebar h2::after \{[^}]+\}", "", content)

# Sidebar ID
content = re.sub(r"content: \"ID-S0NN // STATUS: ACTIVE\";", "content: \"UNIVERSITY OF SCIENCE // VNU\";\n    font-family: var(--font-body);\n    font-weight: 500;", content)

# Nav
content = re.sub(r"background: rgba\(8, 8, 8, 0\.85\);", "background: rgba(13, 17, 23, 0.85);", content)
content = re.sub(r"letter-spacing: 0\.1em;", "letter-spacing: 0.05em;", content)

# Headings
content = re.sub(r"letter-spacing: -0\.05em;", "letter-spacing: -0.02em;", content)

with open('styles.css', 'w') as f:
    f.write(content)
