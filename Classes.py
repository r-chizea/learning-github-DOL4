class Student:

    def __init__(self, name, age, form):
        self.name = name
        self.age = age
        self.form = form
    
    def testAvg(self, testScores):
        total = 0
        for test in testScores:
            total += test
        
        return total / len(testScores)


stu1 = Student('Thomas', 16, '1A')
stu2 = Student('Joe', 15, '2B')
    
print(stu2.age)

scores = [75, 89, 94]

print(stu1.testAvg(scores))
