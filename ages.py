"This is a file for the list lab. I will be sorting through ages and running for loops on them."

ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7, 9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25 ,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

AGES_LEN = len(ages)

# for age in ages:
#    print(age)

for i in range(AGES_LEN):
    ages[i] += 1

ages = [age for age in ages if 16 < age < 65]

# print(ages)

COUNTER = 0

for age in ages:
    if 16 < age < 25:
        COUNTER += 1

print(COUNTER)

ages.sort()

print(ages)

young_adults = len(ages) / COUNTER

print(young_adults)
