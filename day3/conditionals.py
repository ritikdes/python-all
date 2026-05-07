# # Task 1
# print(bool(0) )
# print(bool(1))
# print(bool(""))
# print(bool("hello"))
# print(bool(None))
# print(bool([]))
# print(bool(0.0))
# print(bool("False"))   # careful with this one


# # Bug 1
# score = 85
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")

# Bug 2
password = ""
if  password:
    print("Password accepted")
else:
    print("Password cannot be empty")

# Bug 3
x = 5
if x > 3 and x > 10:
    print("Big number")


# Task 3
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


username = input("Enter username: ")
password = input("Enter password: ")

if " " in username or len(username) < 4:
    print("Username error")
elif len(password) < 8 or not any(char.isdigit() for char in password):
    print("Password error")
else:
    print("login successful")


x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    print(x + y)
elif operator == "-":
    print(x - y)
elif operator == "*":
    print(x * y)
elif operator == "/":
    if y != 0:
        print(x / y)
    else:
        print("Cant divide by zero")
else:
    print("Invalid operator")


