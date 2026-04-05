import os

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Awesome DESIGN.md Examples</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: -apple-system, system-ui, sans-serif; padding: 20px; max-width: 800px; margin: 0 auto; line-height: 1.6; }
        h1 { border-bottom: 1px solid #ccc; padding-bottom: 10px; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; padding: 10px; background: #f5f5f5; border-radius: 5px; }
        a { text-decoration: none; color: #0366d6; font-weight: 500; }
        a:hover { text-decoration: underline; }
        .links { display: flex; gap: 15px; margin-top: 5px; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>Awesome DESIGN.md Examples</h1>
    <ul>
"""

designs = sorted([d for d in os.listdir("design-md") if os.path.isdir(os.path.join("design-md", d))])

for d in designs:
    html += f"""
        <li>
            <strong style="text-transform: capitalize;">{d}</strong>
            <div class="links">
                <a href="/design-md/{d}/preview.html">Light Preview</a>
                <a href="/design-md/{d}/preview-dark.html">Dark Preview</a>
                <a href="/design-md/{d}/DESIGN.md">DESIGN.md</a>
            </div>
        </li>
"""

html += """
    </ul>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html)
