import json
import os
from flask import Flask, render_template, request, redirect, flash, Blueprint, url_for

todo_bp = Blueprint("todo", __name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
DATA_FILE = os.path.join(PROJECT_ROOT, "tasks.json")

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
    
def load_tasks():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        return []

@todo_bp.route("/")
def show_all_tasks():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@todo_bp.route("/add", methods=["POST"])
def add_task():
    tasks = load_tasks()
    task_name = request.form.get("task_name").strip()
    category = request.form.get("category")
    if task_name:
        new_id = tasks[-1]["id"] + 1 if tasks else 1
        new_task = {
            "id": new_id,
            "name": task_name,
            "done": False,
            "category": category
        }
        tasks.append(new_task)
        save_tasks(tasks)
        flash("Task added!", "Success")
    else:
        flash("Task name cannot be empty!", "error")

    return redirect(url_for("todo.show_all_tasks"))

@todo_bp.route("/category/<name>")
def filter_by_category(name):
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if task.get("category") == name]
    return render_template("index.html", tasks=filtered_tasks, current_category=name)

# Mark task as done
@todo_bp.route("/done/<int:task_id>", methods=["POST"])
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            break
    save_tasks(tasks)
    flash("Task marked as done!", "succcess")

    return redirect(url_for("todo.show_all_tasks"))

# Delete task
@todo_bp.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    flash("Task deleted!", "info")
    
    return redirect(url_for("todo.show_all_tasks"))

@todo_bp.route("/about")
def about():
    return render_template("about.html")