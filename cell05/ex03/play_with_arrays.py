#!/bin/python3
number = [2, 8, 9, 48, 8, 22, -12, 2]
print(number)

new_number = set([x for x in number if x > 5])
result = [x + 2 for x in new_number]
print(result)