#!/usr/bin/python3
import random
number = random.randint(-10, 10)
def check_number():
    if number > 0:
        print(f"{number} Is positive")
    elif  number < 0:
        print(f"{number} Is negative")
    else: 
        print(f"{number} Is zero")

check_number()