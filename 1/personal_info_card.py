name = input("Enter your name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
study_field = input("Enter your field of study: ")
hobby = input("What is your hobby? ")

year = 2026 - age

print("=============================")
print("       STUDENT PROFILE")
print("=============================")
print(f"Name    : {name}")
print(f"Age     : {age} (Born in {year})")
print(f"City    : {city}")
print(f"Field   : {study_field}")
print(f"Hobby   : {hobby}")
print("=============================")