import os
import json
from datetime import date
from flask import Flask,Response, Blueprint, render_template, flash, request, redirect, url_for

expense_bp = Blueprint("expense", __name__)

FILENAME = "expenses.json"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
DATA_FILE = os.path.join(PROJECT_ROOT, FILENAME)

CATEGORIES = ["Food", "Transport", "Utilities", "Entertainment", "Shopping", "Other"]

def load_expenses():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        return []
    
def save_expenses(expense):
    with open(FILENAME, "w") as f:
        json.dump(expense, f, indent=4)


@expense_bp.route("/", methods=["GET"])
def show_all_expenses():
    expenses = load_expenses()
    return render_template("index.html", expense=expenses)        

@expense_bp.route("/add", methods=["GET"])
def show_form():
    expenses = load_expenses()
    return render_template("add.html", categories=CATEGORIES)

@expense_bp.route("/add", methods=["POST"])
def add_expense():
    expense = load_expenses()

    amount = request.form.get("amount")
    category = request.form.get("category")
    description = request.form.get("description")

    if amount and category:
        amount = int(amount)
        new_id = expense[-1]["id"] + 1 if expense else 1
        new_expense = {
            "id": new_id,
            "date": str(date.today()),
            "category": category,
            "amount": amount,
            "description": description
        }
        expense.append(new_expense)
        save_expenses(expense)
        flash("Expense added!")
    else:
        flash("Expense cannot be added!")
    return redirect("/")

@expense_bp.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit_expense(expense_id):
    expenses = load_expenses()
    if request.method == "GET":
        target_expense = None
        for expense in expenses:
            if expense["id"] == expense_id:
                target_expense = expense
                break
        return render_template("edit.html", expense=target_expense, categories=CATEGORIES)

    if request.method == "POST":
        amount = request.form.get("amount")
        amount = int(amount)
        category = request.form.get("category")
        description = request.form.get("description")

        for item in expenses:
            if item["id"] == expense_id:
                item["amount"] = amount
                item["category"] = category
                item["description"] = description
                break
            
        save_expenses(expenses)
        flash("Edited sucessfully!")
    else:
        flash("Cannot be edited!")
    return redirect("/")

@expense_bp.route("/filter", methods=["GET"])
def filter_by_date():
    expenses = load_expenses()
    filtered_expenses = []
    # if request.args:
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    if start_date and end_date:
        filtered_expenses = [item for item in expenses if start_date <= item["date"] <= end_date]
    else:
        flash("Cannot find")
    return render_template("filter.html", expense=filtered_expenses)

@expense_bp.route("/export", methods=["GET"])
def export_to_csv():
    expenses = load_expenses()
    def generate():
        # Yield the csv header row
        yield "ID,Date,Category,Amount,Description\n"
        # Loop through expenses and yield each row with commas
        for e in expenses:
            yield f"{e['id']}.{e['date']},{e['category']},{e['amount']},{e['description']}"

    return Response(generate(), mimetype="text/csv", headers={"Content-Disposition": "attachement;filename=expenses.csv"})
  

@expense_bp.route("/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    expenses = load_expenses()
    expenses = [expense for expense in expenses if expense["id"] != expense_id]
    save_expenses(expenses)
    flash("Expense deleted!", "info")

    return redirect("/")

@expense_bp.route("/summary", methods=["GET"])
def show_summary():
    expenses = load_expenses()
    total_spent = sum(item["amount"] for item in expenses)
    category_totals = {cat: 0 for cat in CATEGORIES}

    for item in expenses:
        if item["category"] in category_totals:
            category_totals[item["category"]] += item["amount"]

    highest_expense = max(expenses, key=lambda x: x['amount']) if expenses else None
    return render_template("summary.html", total=total_spent, breakdown=category_totals, highest=highest_expense)

@expense_bp.route("/category/<name>", methods=["GET"])
def show_expenses_by_category(name):
    expenses = load_expenses()
    same_category = [expense for expense in expenses if expense["category"] == name]
    return render_template("index.html", expense=same_category)
