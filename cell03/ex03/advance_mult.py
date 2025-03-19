#!/usr/bin/env python3
multiplier = 0
while multiplier <= 10:
    print(f"Table de {multiplier}: ", end = "")

    current_number = 0
    while current_number <= 10:
        print(multiplier * current_number, end = " ")
        current_number += 1
    
    print()
    multiplier += 1