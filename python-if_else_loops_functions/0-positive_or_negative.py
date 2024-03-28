#!/usr/bin/python3
import random
number = random.randint(-10, 10)
def check_number():
    if number > 0:
        print("Is positive")
    elif  number < 0:
        print("Is negative")
    else: 
        print("Is zero")

check_number()