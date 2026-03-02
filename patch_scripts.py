import re

with open('scripts.js', 'r') as f:
    content = f.read()

# Make particles blue/cyan and slower
content = re.sub(
    r"this\.vx = \(Math\.random\(\) - 0\.5\) \* \(0\.6 / this\.layer\);",
    "this.vx = (Math.random() - 0.5) * (0.2 / this.layer);",
    content
)
content = re.sub(
    r"this\.vy = \(Math\.random\(\) - 0\.5\) \* \(0\.6 / this\.layer\);",
    "this.vy = (Math.random() - 0.5) * (0.2 / this.layer);",
    content
)

# Particle color (from white to cyan/blue)
content = re.sub(
    r"ctx\.fillStyle = `rgba\(255, 255, 255, \$\{this\.alpha\}\)`;",
    "ctx.fillStyle = `rgba(88, 166, 255, ${this.alpha})`;", # var(--accent-color)
    content
)

# Line color
content = re.sub(
    r"this\.ctx\.strokeStyle = `rgba\(255, 255, 255, \$\{\(1 - dist / limit\) \* 0\.1 / p\.layer\}\)`;",
    "this.ctx.strokeStyle = `rgba(88, 166, 255, ${(1 - dist / limit) * 0.15 / p.layer})`;",
    content
)

# Remove text scramble usage
content = re.sub(
    r"const headings = entry.target.querySelectorAll\('h1, h2, h3'\);\n                headings.forEach\(h => \{\n                    const fx = new TextScramble\(h\);\n                    fx\.setText\(h\.innerText\);\n                \}\);",
    "",
    content
)

with open('scripts.js', 'w') as f:
    f.write(content)
