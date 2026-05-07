full_name = input("Enter Full name: ")
email = input("Enter email: ")
phone_num = input("Enter Phone Number: ")
city = input("Enter your city: ")

full_name = full_name.strip().title()
email = email.strip().lower()
phone_num = phone_num.strip()
city = city.strip()

valid = False
if "@" in email and "." in email:
    valid = True

formatted_phone = f"{phone_num[:3]}-{phone_num[3:6]}-{phone_num[6:]}"

if valid:
    print("=========================")
    print("      CONTACT CARD")
    print("=========================")
    print(f"Name    : {full_name}")
    print(f"Email   : {email}")
    print(f"Phone   : {formatted_phone}")
    print(f"City    : {city}")

else:
    print("Invalid email")

# email = "invalidemail"
# if "@" and "." in email:
#     print("valid")