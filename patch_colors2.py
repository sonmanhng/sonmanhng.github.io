import re

with open('styles.css', 'r') as f:
    content = f.read()

# Apply Lora to headings
content = re.sub(
    r"--font-heading: 'Outfit', sans-serif;",
    "--font-heading: 'Lora', serif;",
    content
)
content = re.sub(
    r"--font-body: 'Outfit', sans-serif;",
    "--font-body: 'Inter', sans-serif;",
    content
)
content = re.sub(
    r"--font-mono: 'Space Mono', monospace;",
    "--font-mono: 'Inter', sans-serif;",
    content
)

# TextScramble removal
content = re.sub(r"const fx = new TextScramble\(h\);\n                    fx\.setText\(h\.innerText\);", "", content)

with open('styles.css', 'w') as f:
    f.write(content)
