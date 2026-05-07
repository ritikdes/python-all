def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if y == 0:
        print("Can't divide by zero")
        return None
    else:
        return x / y
    
def power(x,y):
    return x ** y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculator():
    while(True):
        print("=======================")
        print("    CALCULATOR APP")
        print("=======================")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Quit")
        print("=======================")
        choice = input("Enter your choice: ")

        if choice == "6":
            print("Goodbye!")
            break
        
        if choice in ["1","2","3","4","5"]:
            x = get_number("Enter first number(X): ")
            y = get_number("Enter second number(Y): ")

            if choice == "1":
                result = add(x, y)
                print(f"{x} + {y} is {result}")
            elif choice == "2":
                result = sub(x, y)
                print(f"{x} - {y} is {result}")
            elif choice == "3":
                result = mul(x, y)
                print(f"{x} * {y} is {result}")
            elif choice == "4":
                result = div(x, y)
                if result is not None:
                    print(f"{x} / {y} is {result:.2f}")
            elif choice == "5":
                result = power(x, y)
                print(f"{x} ^ {y} is {result}")
        else:
            print("Invalid choice")


calculator()