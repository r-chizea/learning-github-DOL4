max_star_length = int(input("Please enter the number of stars you'd like on your longest line: "))
counter = max_star_length
for i in range(1,(max_star_length * 2)):
    if i <= max_star_length:
        print('* ' * i)
    else:
        counter -= 1
        print('* ' * counter)