# Expense_Tracker.py

import json

def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    expenses.append({"name": name, "amount": amount})
    save_expenses(expenses)
    print(f"Added expense: {name} - ${amount}")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(f"{expense['name']} - ${expense['amount']}")
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total: ${total}")

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")
