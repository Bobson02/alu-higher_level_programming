#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_num = number % 10

def num_printer():

    if number < 0 and abs_num < 6 and abs_num != 0:
        print(f"The last digit of {number} is -{abs_num} and is less than 6 and not 0.")
    elif number > 0 and abs_num < 6 and abs_num != 0:
        print(f"Last digit of {number} is {abs_num} and is less than 6 and not 0.")
    elif abs_num > 6 and abs_num != 0:
        print(f"Last digit of {number} is {abs_num}, which is greater than 6 and not 0.")
    elif abs_num == 6:
        print(f"The last digit of {number} is 6, and it is equal to 6 but not 0.")
       
    else:
        print(f"Last digit of {number} is 0 and is 0")

num_printer()