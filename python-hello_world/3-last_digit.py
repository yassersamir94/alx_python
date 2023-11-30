import random

number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = number % 10

print(f"Last digit of {number} is {last_digit if number >= 0 else -last_digit} and", end=" ")

# Check conditions and print the corresponding message
if abs(last_digit) > 5:
    print("is greater than 5")
elif abs(last_digit) == 0:
    print("is 0")
else:
    print(f"is less than 6 and not 0")
    