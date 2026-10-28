import os
import json
from datetime import date
from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for

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