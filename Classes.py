from abc import ABCMeta, abstractmethod

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

class Bird(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def can_fly(self):
        pass

class Owl(Bird):

    def can_fly(self):
        print(f"{self.name} is an owl and can fly.")

class Dodo(Bird):

    def can_fly(self):
        print(f"{self.name} is a dodo and can't fly.")

bird1 = Owl("Hootie")
bird2 = Dodo("Squawkie")

bird1.can_fly()
bird2.can_fly()