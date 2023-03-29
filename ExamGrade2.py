level = int(input("enter your level: "))
examMark = int(input("enter the exam mark: "))

if level < 1 or level > 2:
    print("Level not Valid.")
elif level == 1:
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
elif level == 2:
    if examMark < 1 or examMark > 100:
        print("Error: mark must be between 1 and 100.")
    elif examMark < 40:
        print("Fail")
    elif examMark  <= 50:
        print("Pass")
    elif examMark <= 65:
        print("Merit")
    else:
        print("Distinction")