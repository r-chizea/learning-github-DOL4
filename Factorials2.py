total = 1
counter = 1
for i in range(1, (int(input("please enter a number: ")) + 1)):
    total *= counter
    counter += 1

print(f"The factorial of the number you entered is: {total}")