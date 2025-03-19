# import json
# import sys
# from datetime import datetime
# import subprocess

# # File path where data will be stored
# data_file = "datastore.json"

# # Function to load data from the file
# def load_data():
#     try:
#         with open(data_file, "r") as file:
#             data = json.load(file)
#     except FileNotFoundError:
#         data = {"income": [], "expenses": []}
#     return data

# # Function to save data back to the file
# def save_data(data):
#     with open(data_file, "w") as file:
#         json.dump(data, file, indent=4)

# # Function to add income to the JSON file
# def add_income(amount, source):
#     data = load_data()  # Load existing data
#     income_entry = {
#         "amount": amount,
#         "date": datetime.now().strftime("%Y-%m-%d"),
#         "source": source
#     }
#     data["income"].append(income_entry)  # Add new income entry
#     save_data(data)  # Save the updated data back to the file
#     print(f"Added income: {amount} from {source}")

# # Function to add expense to the JSON file
# def add_expense(amount, category, description):
#     data = load_data()  # Load existing data
#     expense_entry = {
#         "amount": amount,
#         "date": datetime.now().strftime("%Y-%m-%d"),
#         "category": category,
#         "description": description
#     }
#     data["expenses"].append(expense_entry)  # Add new expense entry
#     save_data(data)  # Save the updated data back to the file
#     print(f"Added expense: {amount} for {category}")

# # Function to be run first (simulate some pre-program logic)
# def run_first():
#     print("Running the first part of the program...")
#     # Here you could add any setup or pre-execution code you want before the main logic.
#     # You can also run an external script here if needed.

#     # Running a second Python script (external script) before continuing
#     subprocess.run(["python", "security.py"])

# # Function to be run second (the main logic of your program)
# def run_second():
#     print("Running the second part of the program...")
#     # You could perform more main logic or simply continue with the main part of your program here.

#     # You can also run another script if needed.
#     subprocess.run(["python", "file2.py"])

# # Displaying the menu options
# def show_menu():
#     print("\n===== Menu =====")
#     print("1. Add Income")
#     print("2. Add Expense")
#     print("3. Exit")

# # Function to handle user input for adding income
# def handle_add_income():
#     amount = input("How much surplus do you want to add?: ")
#     try:
#         amount = float(amount)  # Convert input to a float for adding income
#         add_income(amount, "Salary")  # Call the correct add_income function
#     except ValueError:
#         print("Please enter a valid number for the amount.")

# # Function to handle user input for adding expense
# def handle_add_expense():
#     amount = input("How much expenses do you want to add?: ")
#     try:
#         amount = float(amount)
#         add_expense(amount, "Food", "General expenses")  # Default category and description
#     except ValueError:
#         print("Please enter a valid number for the amount.")

# # Main program loop
# if __name__ == "__main__":
#     run_first()  # Run the first part (which will also run security.py)
#     run_second()  # Run the second part (which will also run file2.py)

#     while True:
#         show_menu()  # Display menu options

#         choice = input("Choose an option (1/2/3): ").strip()

#         if choice == "1":
#             handle_add_income()  # Handle income addition
#         elif choice == "2":
#             handle_add_expense()  # Handle expense addition
#         elif choice == "3":
#             print("Exiting the program.")
#             sys.exit()  # Exit the program
#         else:
#             print("Invalid choice. Please enter '1', '2', or '3'.")

        
    


#Channel log -1
##Add calculator to all budget surplus and expenses for accounting and numbers purposes.
###Note: Not finished yet;
####-Add calculator
####-Add daily budget planner
####-Add car savings and goals budget data saving planner
#####(Add all to the json information database)
#####All information should eventually be encrypted and mmoved to a json infermational database file for compilation

##Channel log -2
###Made menu options for the monthly bedget, etc.
######GOT TO MAKE A PYTON CALCULATOR

import json
import sys
from datetime import datetime
import subprocess

# File path where data will be stored
data_file = "datastore.json"

# Function to load data from the file
def load_data():
    try:
        with open(data_file, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"income": 0.0, "expenses": []}  # Changed default income to 0.0
    return data

# Function to save data back to the file
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

# Function to set monthly income
def set_income(amount):
    data = load_data()
    data["income"] = amount
    save_data(data)
    print(f"Monthly income set to: {amount}")

# Function to add an expense
def add_expense(amount, category, description):
    data = load_data()
    expense_entry = {
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "description": description
    }
    data["expenses"].append(expense_entry)
    save_data(data)
    print(f"Added expense: {amount} for {category}")

# Function to calculate the remaining budget
def calculate_budget():
    data = load_data()
    total_expenses = sum(expense["amount"] for expense in data["expenses"])
    remaining_budget = data["income"] - total_expenses
    return remaining_budget

# Function to display the menu
def show_menu():
    print("\n===== Budget Calculator Menu =====")
    print("1. Set Monthly Income")
    print("2. Add Expense")
    print("3. View Current Budget")
    print("4. View All Expenses")
    print("5. Remove Data")
    print("6. Exit")

# Function to handle setting monthly income
def handle_set_income():
    amount = input("Enter your monthly income: ")
    try:
        amount = float(amount)
        set_income(amount)
    except ValueError:
        print("Please enter a valid number for the income.")

# Function to handle adding an expense
def handle_add_expense():
    amount = input("Enter the expense amount: ")
    category = input("Enter the category (e.g., Food, Rent, etc.): ")
    description = input("Enter a description of the expense: ")
    try:
        amount = float(amount)
        add_expense(amount, category, description)
    except ValueError:
        print("Please enter a valid number for the expense.")

# Function to handle viewing the current budget
def handle_view_budget():
    remaining_budget = calculate_budget()
    print(f"Remaining Budget for the Month: {remaining_budget}")

# Function to handle viewing all expenses
def handle_view_expenses():
    data = load_data()
    if not data["expenses"]:
        print("No expenses recorded yet.")
    else:
        print("\n===== Expenses =====")
        for expense in data["expenses"]:
            print(f"Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")
            
# Function to be run first (simulate some pre-program logic)
def run_first():
    print("Running the first part of the program...")
    # Here you could add any setup or pre-execution code you want before the main logic.
    # You can also run an external script here if needed.

    # Running a second Python script (external script) before continuing
    subprocess.run(["python", "security.py"])

# Function to be run second (the main logic of your program)
def run_second():
    print("Running the second part of the program...")
    # You could perform more main logic or simply continue with the main part of your program here.

    # You can also run another script if needed.
    subprocess.run(["python", "file2.py"])

# Main program loop
if __name__ == "__main__":
    run_first()  # Run the first part (which will also run security.py)
    run_second()  # Run the second part (which will also run file2.py)

    while True:
        # Show the menu
        show_menu()

        choice = input("Choose an option (1/2/3/4/5): ").strip()

        if choice == "1":
            handle_set_income()  # Handle setting monthly income
        elif choice == "2":
            handle_add_expense()  # Handle adding expense
        elif choice == "3":
            handle_view_budget()  # View current budget
        elif choice == "4":
            handle_view_expenses()  # View all expenses
        elif choice == "5":
            print("Remove data")    
        elif choice == "6":
            print("Exiting the program.")
            sys.exit()  # Exit the program
        else:
            print("Invalid choice. Please enter '1', '2', '3', '4', '5', or '6'.")
