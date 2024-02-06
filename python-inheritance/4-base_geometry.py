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

class BaseGeometry:
    """
    BaseGeometry class represents a base class for geometry operations.

    This class provides a method to raise an exception when the area calculation is not implemented.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the area calculation is not implemented.
        """
        raise Exception("area() is not implemented")

    def __init_subclass__(cls):
        """
        Empty method to prevent implicit addition of __init_subclass__.
        """
        pass
