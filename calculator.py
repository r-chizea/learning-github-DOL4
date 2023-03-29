num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))
print("1. add '+'")
print("2. Subtract '-'")
print("3. multiply '*'")
print("4. divide '/'")
print("5. power 'p'")
operation = (input("enter the symbol of the operation you would like to perform: "))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1/num2)
elif operation == 'p':
    print(num1 ** num2)
else:
    print("invalid operator")
