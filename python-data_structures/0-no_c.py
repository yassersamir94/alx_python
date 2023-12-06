def no_c(my_string):
    # Use a list comprehension to create a new string without 'c' and 'C'
    new_string = ''.join(char for char in my_string if char not in {'c', 'C'})
    return new_string
