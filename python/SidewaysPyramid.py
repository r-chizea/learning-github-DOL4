counter = 0
for i in range(1,10):
    if i <=5:
        print('* ' * i)
    else:
        counter += 1
        print('* ' * (5 - counter))

