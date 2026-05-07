# Task 1
text = "Computer Engineering"

print(text[0])
print(text[-1])
print(text[:8])
print(text[-11:])
print(text[::2])
print(text[::-1])

# Task 2 
user_email = "  JohnDoe@GMAIL.com  "
user_name = "  john doe  "

cleaned_email = user_email.strip().lower()
print(cleaned_email)

print(user_name.strip().title())

if "@" in cleaned_email:
    print("Valid")
else:
    print("Invalid")


print(len(cleaned_email))

# Task 3
full_name = input("Enter full name: ")
parts = full_name.strip().split()
firstname = parts[0]
lastname = parts[-1]
print(f"First name: {firstname}")
print(f"Last Name: {lastname}")

text = input("Enter a sentence: ")
print(len(text))
print(len(text.replace(" ", "")))


print(text[::-1])


username = input("Enter username: ")
if " " in username:
    print("Cannot contain space")
elif len(username) <= 3:
    print("Too short username")
else:
    print("valid username")