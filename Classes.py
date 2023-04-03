from abc import ABCMeta, abstractmethod

class Student:
    _studentID = 1
    
    def __init__(self, name, age, form):
        self.name = name
        self.age = age
        self.form = form
        self._studentID =+1
    
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


class Budget:

    def __init__(self, balance):
        self.balance = balance
    
    def __repr__(self):
        return f"The balance of this budget is {self.balance}"
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount
    
    def transfer_to(self, anotherBudget, amount):
        self.balance -= amount
        anotherBudget.balance += amount
    
    def transfer_from(self, anotherBudget, amount):
        self.balance += amount
        anotherBudget.balance -= amount
    
food = Budget(300.00)
travel = Budget(75.00)
bills = Budget(400.00)

print(food)
print(travel)
print(bills)

travel.withdraw(2.25)
print(travel)

food.deposit(50.74)
print(food)

bills.transfer_from(food, 30)
print(bills)
print(food)

food.transfer_to(travel, 20)
print(food)
print(travel)