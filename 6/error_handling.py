def division():
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter another number: "))
        div = x / y

    except ValueError as v:
        print("Error:", v)
    except ZeroDivisionError:
        print("Can't divide by zero")
    else:
        print(f"{x}/{y} = {div:.2f}")

division()


try:
    with open("missing.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File was not found.")