import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    print(f"Last digit of {number} and is greater than 5")
if last_digit == 0:
    print(f"Last digit of {number} and is 0")
else:
    print(f"Last digit of {number} and is less than 6 and not 0")
