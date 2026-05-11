students = [
    {"name": "Arun", "marks": [85, 90, 78, 92, 88]},
    {"name": "Sara", "marks": [70, 65, 80, 75, 72]},
    {"name": "Raj",  "marks": [95, 98, 92, 96, 99]},
]
top_scorer = None
highest = 0

for student in students:
    marks_list = student["marks"]
    average = sum(marks_list) / len(marks_list)
    print(f"Student Name: {student['name']} | Average: {average:.2f}") # Problem 1

    # Problem 2
    if average  > highest:
        highest = average
        top_scorer = student["name"]
    # Problem 3
    if average >= 90:
        student["grade"] = "A+"
    elif average >= 80:
        student["grade"] = "A"
    elif average >= 70:
        student["grade"] = "B+"
    elif average >= 60:
        student["grade"] = "B"
    elif average >= 50:
        student["grade"] = "C"
    else:
        student["grade"] = "Fail"

    
print()
print(f"Top scorer: {top_scorer} | Average: {highest:.2f}")

print()
print(students)