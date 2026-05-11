# ## Problem 1
# from datetime import date
# name = input("Enter your name: ")
# birth_year = int(input("Enter your birth year: "))

# current_year = date.today().year
# age = current_year - birth_year
# print(f"Hello {name}! You are {age} years old and were born in {birth_year}")

# # Problem 2
# height_cm = float(input("Enter your height in centimeters: "))
# height_inch = height_cm / 2.54
# feet = int(height_inch / 12)
# inch = int(height_inch % 12)

# print(f"You are {feet} ft {inch} inches tall.")

# Problem 3
x = int(input("Enter a number:"))
y = int(input("Enter another number:"))
add = x + y
difference = x - y
product = x * y

print(f"Sum is {add} \n Difference is {difference} \n Product is {product}")
if y!= 0:
    div =x / y
    print(f"Divison is {div:.2f}")
else:
    print("Can't divide by zero")




# print(10 / 0)
# print(int("hello"))
# print("22" + 22)

# x = "5"
# y = 3
# print(x * y)