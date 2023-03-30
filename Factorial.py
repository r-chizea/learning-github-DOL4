from collections import Counter


num = int(input("please enter a number: "))
counter = 1
calc = 1
while counter <= num:
    calc = calc * (counter)
    counter += 1
print(calc)