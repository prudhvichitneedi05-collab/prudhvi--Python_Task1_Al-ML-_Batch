def student_result(name, roll, marks):
    total = sum(marks)
    average = total / 5

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("Student:", name)
    print("Roll:", roll)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)

    for i in range(5):
        if marks[i] < 40:
            print("Below 40 in Subject", i + 1)


name = "Prudhvi"
roll = 5
marks = [78, 35, 67, 92, 40]

student_result(name, roll, marks)
