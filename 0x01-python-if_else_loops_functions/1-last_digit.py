#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if(number < 0):
    lastDigit = int(str(number)[-1]) * -1
else:
    lastDigit = int(str(number)[-1])
first = "Last digit of "
last = " and is less than 6 and not 0"
if(lastDigit > 5):
    print(first + f"{number} is {lastDigit} and is greater than 5")
elif(lastDigit == 0):
    print(first + f"{number} is {lastDigit} and is 0")
else:
    print(first + f"{number} is {lastDigit}" + last)
