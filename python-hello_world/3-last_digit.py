import random
number = random.randint(-10000, 10000)
last_digit = number % 10

print(f"Last digit of {number} is {last_digit if number >= 0 else -last_digit} and", end=" ")

if last_digit > 5:
    print("is greater than 5")
if last_digit == 0:
    print("is 0")
if last_digit < 6 and last_digit !=0 and last_digit <0:
    print("is less than 6 and not 0")
