import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10  # Use abs to get the absolute value of the number

print(f"Last digit of {number} is {last_digit if number >= 0 else -last_digit} and", end=" ")

if last_digit > 5:
    print("is greater than 5")
elif last_digit == 0:
    print("is 0")
else:
    print("is less than 6 and not 0" if number >= 0 else "is less than 6 and not 0")
