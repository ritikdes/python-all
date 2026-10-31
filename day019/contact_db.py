import sqlite3

def get_connection():
    return sqlite3.connect("contacts.db")

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        email TEXT
    ) """)
    conn.commit()
    conn.close()

def add_contact(name, phone, email):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()

def view_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_contact(name_query):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name LIKE ?", (f"%{name_query}%",))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_contact(contact_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()

def main():
    while(True):
        print("-" * 55)
        print(" "*15 + "CONTACT BOOK")
        print("-" * 55)
        print("1. Add contact")
        print("2. View all Contact")
        print("3. Search Contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Enter your choice: ")
        init_db()

        if choice == "1":
            name = input("Enter name: ")

            while(True):
                phone = input("Enter 10 digit phone number: ")
                if len(phone) == 10 and phone.isdigit():
                    break
                print("Invalid phone number!")

            while(True):
                email = input("Enter email: ")
                if "@" in email and "." in email:
                    break
                print("Enter correct email.")

            add_contact(name, phone, email)
            print("Contact added sucessfully!")

        elif choice == "2":
            contacts = view_all()
            if contacts:
                print("-" * 55)
                print(f"{'ID':<3} | {'NAME':<15} | {'PHONE':<12} | {'EMAIL'}")
                print("-" * 55)
                for item in contacts:
                    print(f"{item[0]:<3} | {item[1]:<15} | {item[2]:<12} | {item[3]}")
            else:
                print("Contact empty!")

        elif choice == "3":
            name = input("Enter name: ")
            contacts = search_contact(name)
            if contacts:
                print("-" * 55)
                print(f"{'ID':<3} | {'NAME':<15} | {'PHONE':<12} | {'EMAIL'}")
                print("-" * 55)
                for item in contacts:
                    print(f"{item[0]:<3} | {item[1]:<15} | {item[2]:<12} | {item[3]}")
            else:
                print("Not found!")

        elif choice == "4":
            name = input("Enter name: ")
            contacts = search_contact(name)

            if not contacts:
                print("No contacts found!")
            else:
                print("-" * 55)
                print(f"{'ID':<3} | {'NAME':<15} | {'PHONE':<12} | {'EMAIL'}")
                print("-" * 55)

                valid_ids = []
                for item in contacts:
                    valid_ids.append(item[0])
                    print(f"{item[0]:<3} | {item[1]:<15} | {item[2]:<12} | {item[3]}")

                try:
                    contact_id = int(input("Enter id of the contact to delete: "))
                    if contact_id in valid_ids:
                        delete_contact(contact_id)
                        print("Contact deleted!")
                    else:
                        print("Invalid Id!")
                except ValueError:
                    print("Invalid ID!")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()