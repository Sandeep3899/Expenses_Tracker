import csv
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Function to add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, Bills, etc.): ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense added successfully!")

# Function to view expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\nDate\t\tCategory\tAmount")
            print("-" * 40)
            for row in reader:
                print("\t".join(row))
    except FileNotFoundError:
        print("No expenses found.")

# Function to analyze spending
def analyze_expenses():
    expenses = {}
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[2])
                expenses[category] = expenses.get(category, 0) + amount

        print("\nExpense Analysis:")
        for category, total in expenses.items():
            print(f"{category}: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses found.")

# Main Menu
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Analyze Expenses")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        analyze_expenses()
    elif choice == "4":
        break
    else:
        print("Invalid choice, please try again.")
