import json

FILENAME = "contacts.json"
contacts = []

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        # Converts to dictionary for JSON saving
        return {"name": self.name, "phone": self.phone, "email":self.email}

    def __str__(self):
        return f"{self.name:<15} | {self.phone:<12} | {self.email:<15}"

def load():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            for item in data:
                contacts.append(Contact(
                    item["name"],
                    item["phone"],
                    item["email"],
                ))

    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error: {e}")
        pass


def save():
    with open(FILENAME, "w") as f:
        data = [contact.to_dict() for contact in contacts]
        json.dump(data, f, indent=4)

def add_contact(name, phone, email):
    new_contact = Contact(name, phone, email)
    contacts.append(new_contact)
    save()

def view_all():
    for contact in contacts:
        print(contact)

def search_by_name(name):
    for item in contacts:
        if item.name.lower() == name.lower():
            print(item)
            return
    print("Couldn't find the contact")

def delete_contact(name):
    for item in contacts:
        if item.name.lower() == name.lower():
            contacts.remove(item)
            save()
            return
    print("Couldn't find the contact")

def main():
    while(True):
        print()
        print("-" * 40)
        print(" " * 15 + "CONTACT BOOK" + " " * 15)
        print("-" * 40)
        print()
        print("1. Add contact")
        print("2. View All contact")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name:")

            while(True):
                phone = input("Enter 10 digit phone number: ")
                if len(phone) == 10 and phone.isdigit():
                    break
                print("Invalid number")

            while(True):
                email = input("Enter email: ")
                if "@" in email and "." in email:
                    break
                print("Invalid email")

            add_contact(name, phone, email)
        elif choice == "2":
            view_all()
        elif choice == "3":
            name = input("Enter name: ")
            search_by_name(name)
        elif choice == "4":
            name = input("Enter contact name: ")
            delete_contact(name)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    load()
    main()