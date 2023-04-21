number = 1
while number <= 100:
    sq = number**2
    if sq > 2000:
        break
    print(f"{number} squared is {sq}")
    number += 1
print(f"{number} squared is over 2000")