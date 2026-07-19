def analyze_result(name, roll, marks):
    
    total = sum(marks)
    ave = total / len(marks)

   
    if ave >= 90:
        grade = "A"
    elif ave >= 75:
        grade = "B"
    elif ave >= 60:
        grade = "C"
    elif ave >= 40:
        grade = "D"
    else:
        grade = "Fail"


    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}")
    print(f"Average: {ave:.2f}")
    print(f"Grade: {grade}")

    
    print("Subjects below 40:")
    found = False

    for index, mark in enumerate(marks):
        if mark < 40:
            print(f"Subject {index + 1}")
            found = True

    if not found:
        print("None")



name = input("Enter student name :")
roll = int(input("Enter student roll number :"))
marks = []

for i in range(5):
    mark = float(input(f"Enter Subject {i+1} Mark: "))
    marks.append(mark)


analyze_result(name, roll, marks)
