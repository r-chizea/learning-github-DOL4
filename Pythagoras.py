print("Pythagoras Calculator:")
print("1. Find the length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")
choice = int(input("please select the number of a function: "))

if choice == 1:
    b = int(input("enter length of side B: "))
    c = int(input("enter length of side C: "))
    print("legnth of side A =", c**2-b**2)
elif choice == 2:
    a = int(input("enter length of side A: "))
    c = int(input("enter length of side C: "))
    print("legnth of side B =", c**2-a**2)
elif choice == 3:
    a = int(input("enter length of side A: "))
    b = int(input("enter length of side B: "))
    print("legnth of side C =", a**2+b**2)