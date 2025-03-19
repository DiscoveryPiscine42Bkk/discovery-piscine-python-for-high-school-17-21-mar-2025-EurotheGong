#!/usr/bin/env python3
number = int(input("Please enter the number : "))
if number <= 25:
    while number <= 25:
        print(f"Inside the loop, my variable is {number}")
        number += 1
else:
    print(number)
    print("ERROR")