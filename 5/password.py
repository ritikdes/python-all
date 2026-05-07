def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Must be at least 8 characters")
    if not any(char.isdigit() for char in password):
        errors.append("Must contain at least one digit")
    if not any(char.isupper() for char in password):
        errors.append("Must contain at least one uppercase letter")
    if " " in password:
        errors.append("Cannot contain space")
     
    return {"valid": len(errors) ==0, "errors":errors}


password = input("Enter your password:")
print(validate_password(password))