tasks = []

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
        task = input("Enter task: ").strip()
        if task == "":
            print("Task cannot be empty")
        else:
            tasks.append({"name":task, "done":False})
            print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for i, task in enumerate(tasks):
                status = "[DONE]" if task["done"] else "[PENDING]"
                print(f"{i+1}. {status} {task['name']}")

    elif choice == "3":
        task_no = int(input("which task to be marked? "))
        if task_no < 1 or task_no > len(tasks):
            print("Invalid task number.")
        else:
            tasks[task_no - 1]["done"] = True
            print("Task marked as done")

    elif choice == "4":
        task_no = int(input("Which task to delete? "))
        if task_no < 1 or task_no > len(tasks):
            print("Invalid task number.")
        else:
            tasks.pop(task_no - 1)
            print("Task deleted")

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid choice")