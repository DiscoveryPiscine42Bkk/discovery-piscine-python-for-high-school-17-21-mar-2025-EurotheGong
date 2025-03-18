first_number = int(input("please enter the first number : "))
second_number = int(input("please enter the secont number : "))
result = int(first_number * second_number)
print(f"{first_number} x {second_number} = {result}")
if result > 0:
    print("The result is positive")
elif result < 0:
    print("The result is negative")
else:
    print("The result is positive and negative")