"This is a file for the list lab. I will be sorting through ages and running for loops on them."

ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7, 9]

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
