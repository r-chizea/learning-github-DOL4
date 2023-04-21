examMark = int(input("enter the exam mark: "))

if examMark < 1 or examMark > 100:
    print("Error: mark must be between 1 and 100.")
elif examMark < 50:
    print("Fail")
elif examMark  <= 60:
    print("Pass")
elif examMark <= 70:
    print("Merit")
else:
    print("Distinction")