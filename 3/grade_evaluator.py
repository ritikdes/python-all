marks = []
name = input("Enter name: ")
for i in range(5):
    mark = int(input(f"Enter marks of for subject {i+1}: "))
    if mark > 100 or mark < 0:
        print("Error")
        exit()
    marks.append(mark)

total = sum(marks)

average = total / 5
print(f"Total: {total}")
print(f"Average: {average}")

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B+"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"


marks_str = ", ".join(str(m) for m in marks)
print("=====================================")
print("        STUDENT RESULT CARD")
print("=====================================")
print(f"Name     : {name}")
print(f"Marks    : {marks_str}")
print(f"Total    : {total}")
print(f"Average  : {average:.2f}%")
print(f"Grade    : {grade}")
    

if grade != "Fail":
    print("Note: Keep it up")
else:
    print("Note: Student needs improvement in weak subjects")