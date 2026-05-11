def celsius_to_fahrenheit(c):
    return (c * 1.8) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * (5 / 9)

def convert_temp(value, unit):
    if unit.upper() == "C":
        return celsius_to_fahrenheit(value)
    elif unit.upper() == "F":
        return fahrenheit_to_celsius(value)
    else:
        return None


value = int(input("Enter temperature: "))
unit = input("Enter unit(C/F): ")

result = convert_temp(value, unit)
if result:
    print(f"Result:  {result:.2f}")
else:
    print("Invalid unit")