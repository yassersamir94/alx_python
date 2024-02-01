"""This module defines the Square class.

The Square class represents a square shape with a given size.

Example:
    # Create a square with size 3
    my_square = Square(3)
    print(my_square.area())  # Output: 9
"""
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ python3 0-main.py
<class '0-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/$ 

class Square:
    """Represents a square shape with a given size.

    Attributes:
        __size (int): Private instance attribute representing the size of the square.
    """

    def __init__(self, size):
        """Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
