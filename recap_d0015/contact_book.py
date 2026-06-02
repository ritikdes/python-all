import json

FILENAME  = "contacts.json"
data = {}

def add_contact(name, number, email):
    if name in data:
        print(f"{name} already exists!")
        return
    data[name] = {
        "phone": number,
        "email": email
    }
    save_contact(data)
    print("Contact saved successfully!")

def search_by_name(name):
    if name in data:
        phone = data[name]['phone']
        email = data[name]['email']
        print(f"Name: {name:<15} Number: {phone:<15} Email: {email:<15}")
    else:
        print(f"{name} doesn't exist.")   

def delete_contact(name):
    if name in data:
        del data[name]
        save_contact(data)
        print(f"{name} deleted successfully.")
    else:
        print(f"{name} does not exists.")
    

def save_contact(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

def load_contact():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error: {e}")
        pass
    return data

def view_all_contact():
    if not data:
        print("No contacts yet.")
        return
    print(f"{'NAME':<15} {'PHONE':<15} {'EMAIL':<15}")
    for name, details in data.items():
        print(f"{name:<15} {details['phone']:<15} {details['email']:<15}")


data = load_contact()

while(True):
    print("-"*30)
    print("----------CONTACTS----------")
    print("1. Add contacts")
    print("2. Search by name")
    print("3. Delete contact")
    print("4. View all contacts")
    print("5. Quit")
    print()

    choice = input("Enter your choice: ")
    if choice == "5":
        print("Goodbye!")
        break
    elif choice == "1":
        number = input("Enter the number:")
        if len(number) == 10 and number.isnumeric():
            name = input("Enter the name: ")
            email = input("Enter the email: ")
            add_contact(name, number, email)
        else:
            print("Invalid number")
    elif choice == "2":
        name = input("Enter name to search: ")
        search_by_name(name)
    elif choice == "3":
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    elif choice == "4":
        view_all_contact()