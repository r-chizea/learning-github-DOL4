import statistics

data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51, 72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47, 48,49,53,61,63,69,75,77,60,83"

grades = data.split(',')

grades = list(map(int, grades))

lowest_grade = min(grades)

print(lowest_grade)

highest_grade = max(grades)

print(highest_grade)

grades_avg = round((sum(grades) / len(grades)), 2)

print(grades_avg)

grades_mean = round(statistics.mean(grades), 2)
print(grades_mean)

grades_median = statistics.median(grades)

print(grades_median)

print(f"The lowest grade was {lowest_grade}. The highest grade was {highest_grade}. The average grade was {grades_avg}. The mean grade was {grades_mean}. The median grade was {grades_median}.")

