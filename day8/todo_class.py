class Task:
    def __init__(self, name):
        self.name = name
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "[DONE]" if self.done else "[PENDING]"
        return f"{status} {self.name}"
    
filename = "tasks_v2.txt"

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
                t = Task(parts[0])
                t.done = parts[1] == "DONE"
                tasks.append(t)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"ERROR: {e}")
    return tasks

def save_tasks(filename,tasks):
    with open(filename, "w") as f:
        for task in tasks:
            status = "DONE" if task.done else "PENDING"
            f.write(f"{task.name}|{status}\n")

def add_task(tasks):
    task = input("Enter task: ").strip()
    if task == "":
        print("Task cannot be empty")
    else:
        tasks.append(Task(task))
        save_tasks(filename, tasks)
        print("Task added!")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def mark_done(tasks):
    task_no = get_number("which task to be marked? ")
    if task_no < 1 or task_no > len(tasks):
        print("Invalid task number.")
    else:
        tasks[task_no - 1].mark_done()
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

