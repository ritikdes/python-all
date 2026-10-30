import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS contacts (
#     id  INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone TEXT
# )""")

# cur.execute("INSERT INTO contacts (name, phone) VALUES (?,?)", ("Ram","9876543210"))
# conn.commit()

# cur.execute("SELECT * FROM contacts")
# print(cur.fetchall())

def insert_contact(name, phone):
    cur.execute("INSERT INTO contacts (name, phone) VALUES (?,?)", (name, phone))
    conn.commit()

def list_contact():
    cur.execute("SELECT * FROM contacts")
    return cur.fetchall()

def search_contact(name_query):
    cur.execute("SELECT * FROM contacts WHERE name LIKE ?", (f"%{name_query}%",))
    return cur.fetchall()

def delete_contact(id):
    cur.execute("DELETE FROM contacts WHERE id = ?",(id,))
    conn.commit()


# insert_contact("Shyam", "9632587410")
# insert_contact("Hari", "9513246870")
# list_contact()
# search_contact("Ram")
# delete_contact(2)
print(list_contact())


conn.close()