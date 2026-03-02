import re

with open('styles.css', 'r') as f:
    text = f.read()

# Refine backgrounds and selections
text = re.sub(
    r"::selection \{\n    background: var\(--primary-color\);\n    color: var\(--bg-color\);\n\}",
    "::selection {\n    background: var(--accent-color);\n    color: var(--bg-color);\n}",
    text
)

# TextScramble cleanup
text = re.sub(
    r"\/\* Text Scramble Effect \*\/[\s\S]*?\}",
    "",
    text
)
# Fix remaining class Dud
text = re.sub(
    r"class=\{\?\}\"dud\"\>\{\?\}",
    "",
    text
)

text = re.sub(
    r"const fx = new TextScramble\(h\);\n                    fx\.setText\(h\.innerText\);",
    "",
    text
)

# Links hover
text = re.sub(
    r"\.pub-link:hover \{\n    background: var\(--primary-color\);\n    color: var\(--bg-color\);\n\}",
    ".pub-link:hover {\n    background: var(--accent-color);\n    color: var(--bg-color);\n    border-color: var(--accent-color);\n}",
    text
)

with open('styles.css', 'w') as f:
    f.write(text)

with open('scripts.js', 'r') as f:
    text2 = f.read()

text2 = re.sub(
    r"\/\/ Text Scramble Effect[\s\S]*?\/\/ Global Initialization",
    "// Global Initialization",
    text2
)

text2 = re.sub(
    r"const headings = entry\.target\.querySelectorAll\('h1, h2, h3'\);\n                headings\.forEach\(h => \{\n                    const fx = new TextScramble\(h\);\n                    fx\.setText\(h\.innerText\);\n                \}\);",
    "",
    text2
)

with open('scripts.js', 'w') as f:
    f.write(text2)
