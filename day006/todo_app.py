filename = "tasks.txt"

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid option")

def load_tasks(filename):
    tasks = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                tasks.append({"name":parts[0].strip(), "done":parts[1].strip() == "DONE"})
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"ERROR: {e}")
    return tasks

def save_tasks(filename,tasks):
    with open(filename, "w") as f:
        for task in tasks:
            status = "DONE" if task["done"] else "PENDING"
            f.write(f"{task['name']}|{status}\n")

def add_task(tasks):
    task = input("Enter task: ").strip()
    if task == "":
        print("Task cannot be empty")
    else:
        tasks.append({"name":task, "done":False})
        save_tasks(filename, tasks)
        print("Task added!")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for i, task in enumerate(tasks):
            status = "[DONE]" if task["done"] else "[PENDING]"
            print(f"{i+1}. {status} {task['name']}")

def mark_done(tasks):
    task_no = get_number("which task to be marked? ")
    if task_no < 1 or task_no > len(tasks):
        print("Invalid task number.")
    else:
        tasks[task_no - 1]["done"] = True
        save_tasks(filename, tasks)
        print("Task marked as done")

def delete_task(tasks):
    task_no = get_number("Which task to delete? ")
    if task_no < 1 or task_no > len(tasks):
        print("Invalid task number.")
    else:
        tasks.pop(task_no - 1)
        save_tasks(filename, tasks)
        print("Task deleted")

tasks = load_tasks(filename)

while(True):
    print()
    print("===== TODO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark done")
    print("4. Delete task")
    print("5. Quit")
    print("=====================")

    choice = input("Enter your choice(1-5): ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        mark_done(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

