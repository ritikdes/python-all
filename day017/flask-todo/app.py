import json
from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "SECRETKEYY"

filename = "tasks.json"
def save_tasks(tasks):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)
    
def load_tasks():
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        return []

@app.route("/")
def show_all_tasks():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    tasks = load_tasks()
    task_name = request.form.get("task_name").strip()
    if task_name:
        new_id = tasks[-1]["id"] + 1 if tasks else 1
        new_task = {
            "id": new_id,
            "name": task_name,
            "done": False
        }
        tasks.append(new_task)
        save_tasks(tasks)
        flash("Task added!", "Success")
    else:
        flash("Task name cannot be empty!", "error")

    return redirect("/")

# Mark task as done
@app.route("/done/<int:task_id>", methods=["POST"])
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            break
    save_tasks(tasks)
    flash("Task marked as done!", "succcess")

    return redirect("/")

# Delete task
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    flash("Task deleted!", "info")
    
    return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=(True))
