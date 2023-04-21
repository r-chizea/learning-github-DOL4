"A collection of classes for the 'Classes' lab."

from abc import ABCMeta, abstractmethod

class Student:
    "a class that defines a student. An object will contain their name, age, form and student ID."

    _student_id = 1

    def __init__(self, name, age, form):
        self.name = name
        self.age = age
        self.form = form
        self._student_id =+1

    def test_avg(self, test_scores):
        "Takes a list of integers and returns the average of those numbers."
        total = 0
        for test in test_scores:
            total += test

        return total / len(test_scores)


stu1 = Student('Thomas', 16, '1A')
stu2 = Student('Joe', 15, '2B')
  
print(stu2.age)

scores = [75, 89, 94]

print(stu1.test_avg(scores))

class Bird(metaclass=ABCMeta):
    "A parent class for Birds, with a necessary can_fly method."

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def can_fly(self):
        "A necessary method for child classes."


class Owl(Bird):
    "A child class of Bird."

    def can_fly(self):
        print(f"{self.name} is an owl and can fly.")

class Dodo(Bird):
    "Another child class of bird."

    def can_fly(self):
        print(f"{self.name} is a dodo and can't fly.")

bird1 = Owl("Hootie")
bird2 = Dodo("Squawkie")

bird1.can_fly()
bird2.can_fly()


class Budget:
    "A class that lets you manage the balance of a budget."

    def __init__(self, balance):
        self.balance = balance

    def __repr__(self):
        return f"The balance of this budget is {self.balance}"

    def withdraw(self, amount):
        "This method allows you to take away from the budget balance."
        self.balance -= amount

    def deposit(self, amount):
        "This method lets you add to the budget balance."
        self.balance += amount

    def transfer_to(self, another_budget, amount):
        "This method lets you transfer from you current budget to another."
        self.withdraw(amount)
        another_budget.deposit(amount)

    def transfer_from(self, another_budget, amount):
        "This method lets you transfer from another budget to your current."
        self.deposit(amount)
        another_budget.withdraw(amount)

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

class Shape(metaclass=ABCMeta):
    "The parent class for all shapes."
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @abstractmethod
    def perimeter(self):
        "This is a necessary class for defining the perimeter of a shape."

    @abstractmethod
    def area(self):
        "This is a necessary class for defining the area of a shape."

class Square(Shape):
    "A child of the shape class, used for calculating things about squares."
    def __init__(self, length):
        self.length = length

    def perimeter(self):
        return self.length * 4

    def area(self):
        return self.length ** 2

class Rectangle(Shape):
    "A child of the shape class, used for calculating things about rectangles."
    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def area(self):
        return self.length * self.width
