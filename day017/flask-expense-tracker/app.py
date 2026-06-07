import os
import json
from datetime import date
from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "expense-secret-key-2026"

FILENAME = "expenses.json"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, FILENAME)

# Defining 6 static categories globally
CATEGORIES = ["Food", "Transport", "Utilities", "Entertainment", "Shopping", "Other"]


def load_expenses():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        return []
    
    
def save_expenses(expense):
    with open(DATA_FILE, "w") as f:
        json.dump(expense, f, indent=4)


@app.route("/", methods=["GET"])
def show_all_expenses():
    expenses = load_expenses()
    return render_template("index.html", expenses=expenses)


@app.route("/add", methods=["GET"])
def show_form():
    return render_template("add.html", categories=CATEGORIES)


@app.route("/add", methods=["POST"])
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
        flash("Expense cannot be added")
    return redirect("/")


@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    expenses = load_expenses()
    expenses = [expense for expense in expenses if expense["id"] != expense_id]
    save_expenses(expenses)
    flash("Expense deleted!", "info")

    return redirect("/")


@app.route("/summary", methods=["GET"])
def show_summary():
    expenses = load_expenses()
    total_spent = sum(item["amount"] for item in expenses)
    category_totals = {cat: 0 for cat in CATEGORIES}

    for item in expenses:
        if item["category"] in category_totals:
            category_totals[item["category"]] += item["amount"]

    highest_expense = max(expenses, key=lambda x: x['amount']) if expenses else None

    return render_template("summary.html", total=total_spent, breakdown=category_totals, highest=highest_expense)


@app.route("/category/<name>", methods=["GET"])
def show_expenses_by_category(name):
    expenses = load_expenses()
    same_category = [expense for expense in expenses if expense["category"] == name ]
    return render_template("index.html", expenses=same_category)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5500)
    # app.run(debug=(True))