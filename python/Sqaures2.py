for i in range(1, 101):
    sq = i**2
    if sq > 2000:
        print(f"{i}^2 is greater than 2000.")
        break
    else:
        print(f"{i}^2 = {sq}")