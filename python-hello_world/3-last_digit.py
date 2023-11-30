import random

number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = number % 10

print(f"Last digit of {number} is {last_digit if number >= 0 else -last_digit} and", end=" ")

# Check conditions and print the corresponding message
if number < 0 and abs(last_digit) < 6 and last_digit != 0:
    print(f"is less than 6 and not 0 and is negative")
elif last_digit == 0:
    print("is 0")
else:
    print("is greater than 5")
    