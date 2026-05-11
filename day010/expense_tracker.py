import os
import json
from datetime import date

FILENAME = "expenses.json"
CATEGORIES = ["Food", "Transport", "Entertainment", "Health", "Shopping", "Other"]

class Expense:
    def __init__(self, id, amount, category, description, date):
        self.id = id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def to_dict(self):
        # Converts to dictionary for JSON saving
        return {"id": self.id, "amount":self.amount, "category":self.category, "description":self.description, "date":self.date}
    
    def __str__(self):
        return f"{self.id:<4} | {self.date:<12} | {self.category:<15} | {self.amount:<10.2f} | {self.description}"
    

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.next_id = 1
        self.load()


    def load(self):
        try:
            with open(FILENAME, "r") as f:
                data = json.load(f) 
                # data is a list of dictionaries
                # Convert each dict back into an Expense object
                for item in data:
                    self.expenses.append(Expense(
                        item["id"],
                        item["amount"],
                        item["category"],
                        item["description"],
                        item["date"]
                    ))
                # Restore next_id 
                if self.expenses:
                    self.next_id = max(e.id for e in self.expenses) + 1
                    
        except FileNotFoundError:    
            pass
        except Exception as e:
            print(f"Error: {e}")
            pass


    def save(self):
        with open(FILENAME, "w") as f:
            save_expense = [item.to_dict() for item in self.expenses]
            json.dump(save_expense, f, indent=4)


    def add_expense(self):
        # Category selection
        for i, cat in enumerate(CATEGORIES):
            print(f"{i+1}. {cat}")
        
        try:
            cat_choice = int(input("Select category(1-6): "))
            if 1 <= cat_choice <= len(CATEGORIES):
                category = CATEGORIES[cat_choice - 1]
            else:
                print("Out of bound choice. Defaulting to 'Other'")
                category = "Other"
        except ValueError:
            print("Invalid category. Defaulting to 'Other'")
            category = "Other"

        # amount validation
        while True:
            try:
                amount = float(input("Enter expense amount: "))
                if amount <= 0:
                    print("Amount must be greater than 0!")
                    continue
                break
            except ValueError:
                print("Enter valid number!")
                pass

        description = input("Enter expense description: ").strip()
        new_expense = Expense(self.next_id, amount, category, description, date.today().isoformat())
        self.expenses.append(new_expense)
        self.next_id += 1
        self.save()
        print(f"Expense {category} saved successfully!")


    def view_all(self):
        total = 0
        if not self.expenses:
            print("No expense yet.")
        else:
            header = f"{'ID':<4} | {'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}"
            print(header)
            print("-" * len(header))
            for expense in self.expenses:
                print(expense)
                total += expense.amount
            print("-" * len(header))
            print(f"{'Total':>34}: {total:>10.2f}")


    def view_by_category(self):
        for i, cat in enumerate(CATEGORIES):
            print(f"{i+1}. {cat}")
        
        try:
            choice = int(input(f"Pick which category to view(1-{len(CATEGORIES)}): "))
            if  not 1 <= choice <= len(CATEGORIES):
                print("Invalid choice")
                return
            
            category = CATEGORIES[choice - 1]

            filtered_expenses = [e for e in self.expenses if e.category == category]
            if not filtered_expenses:
                print(f"No expenses found in {category}")
                return
            
            print(f"\n------------------ {category.upper()} EXPENSES ----------------") 
            header = f"{'ID':<4} | {'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}"
            for e in filtered_expenses:
                print(e)
            
            subtotal = sum(e.amount for e in filtered_expenses)
            print("-" * 50)
            print(f"{'Subtotal':<36}: Rs{subtotal:.2f}")

        except ValueError:
            print("Invalid selection")



    def view_summary(self):
        category_totals ={}
        total_spent= 0
        if not self.expenses:
            print("No expenses yet.")
            return
        
        for e in self.expenses:
            total_spent += e.amount
            if e.category in category_totals:
                category_totals[e.category] += e.amount
            else:
                category_totals[e.category] = e.amount

        print("Summary")
        print(f"Total Spent: Rs.{total_spent:.2f}")
        for category, amount in category_totals.items():
            percentage = (amount / total_spent) * 100
            print(f"{category:<15}: Rs.{amount:<10.2f} ({percentage:.1f}%)")
        
        highest_expense = max(self.expenses, key=lambda e: e.amount)
        current_month = date.today().isoformat()[:7]
        month_total = sum(e.amount for e in self.expenses if e.date.startswith(current_month))

        print(f"Highest Expense: Rs.{highest_expense.amount:<15.2f} - {highest_expense.category} - {highest_expense.description}")
        print(f"This month : Rs.{month_total:.2f}")



    def delete_expense(self):
        self.view_all()
        target_id = int(input("Enter the ID of expense to be deleted: "))
        for e in self.expenses:
            if e.id == target_id:
                confirm = input("Are you sure? (y/n): ").strip().lower() 
                if confirm == "y":
                    self.expenses.remove(e)
                    print("Expense deleted successfully.")
                    self.save()
                    break
                else:
                    return
        else:
            print("Invalid ID!")


def main():
    tracker = ExpenseTracker()
    while True:
        print()
        print("============================")
        print("      EXPENSE TRACKER")
        print("============================")
        print("1. Add Expense")
        print("2. View all Expenses")
        print("3. View by Category")
        print("4. View Summary")
        print("5. Delete Expense")
        print("6. Quit")
        print("=============================")
        choice = input("Enter your choice: ")

        if choice == "6":
            print("Goodbye!")
            break
        elif choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_all()
        elif choice == "3":
            tracker.view_by_category()
        elif choice == "4":
            tracker.view_summary()
        elif choice == "5":
            tracker.delete_expense()
        else:
            print("Invalid choice!")

main()