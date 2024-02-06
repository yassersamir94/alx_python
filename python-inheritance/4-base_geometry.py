#!/usr/bin/python3
"""Module for BaseGeometry class"""

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1 style="text-transform: uppercase;">Title</h1>
</body>
</html>
"""

with open("output.html", "w") as f:
    f.write(html_content)