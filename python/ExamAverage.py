def examAverage():
    grades = []
    total = 0
    average = 0

    for grade in int(input("Please enter your Maths grade: ")):
        if grade < 0 or grade > 100:
            print("Invalid grade - grade must be between 0 and 100.")
            continue
        else:
            grades.append(mGrade)

    eGrade = int(input("Please enter your English grade: "))
    for grade in eGrade:
        if grade < 0 or grade > 100:
            print("Invalid grade - grade must be between 0 and 100.")
            continue
        else:
           grades.append(eGrade)

    iGrade = int(input("Please enter your Maths grade: "))
    for grade in iGrade:
        if grade < 0 or grade > 100:
            print("Invalid grade - grade must be between 0 and 100.")
            continue
        else:
           grades.append(iGrade)

    for grade in grades:
        total += grade

    average = total / 3

    if average < 65:
        print(f"Your average score is {average}. This is a fail.")
    else:
        print(f"Your average score is {average}. This is a pass.")

examAverage()