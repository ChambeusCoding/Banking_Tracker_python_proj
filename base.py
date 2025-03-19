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
        data = {"income": [], "expenses": []}
    return data

# Function to save data back to the file
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

# Function to add income to the JSON file
def add_income(amount, source):
    data = load_data()  # Load existing data
    income_entry = {
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "source": source
    }
    data["income"].append(income_entry)  # Add new income entry
    save_data(data)  # Save the updated data back to the file
    print(f"Added income: {amount} from {source}")

# Function to add expense to the JSON file
def add_expense(amount, category, description):
    data = load_data()  # Load existing data
    expense_entry = {
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "description": description
    }
    data["expenses"].append(expense_entry)  # Add new expense entry
    save_data(data)  # Save the updated data back to the file
    print(f"Added expense: {amount} for {category}")

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

# Main program
if __name__ == "__main__":
    run_first()  # Run the first part (which will also run file1.py)
    run_second()  # Run the second part (which will also run file2.py)

    # Ask for user input to add income
    response = input("Do you want to add income? (yes/no): ").strip().lower()

    if response == "yes" or response == "y":
        amount = input("How much surplus do you want to add?: ")
        try:
            amount = float(amount)  # Convert input to a float for adding income
            add_income(amount, "Salary")  # Call the correct add_income function
        except ValueError:
            print("Please enter a valid number for the amount.")
    elif response == "no" or response == "y":
        print("Exiting the program.")
        sys.exit()  # Exit the program
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

    response = input("Do you want to add expenses to budget? (yes/no): ").strip().lower()

    if response == "yes" or response == "y":
        amount = input("How much expenses do want to add?: ")
        try:
            amount = float(amount)
            add_expenses(amount, "Food")
        except ValueError:
            print("Please enter a valid number for the amount.")
    elif response == "no" or response == "y":
        print("Exiting the program.")
        sys.exit() # Exit program again
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


#Channel log -1
##Add calculator to all budget surplus and expenses for accounting and numbers purposes.
###Note: Not finished yet;
####-Add calculator
####-Add daily budget planner
####-Add car savings and goals budget data saving planner
#####(Add all to the json information database)
#####All information should eventually be encrypted and mmoved to a json infermational database file for compilation

##Channel log -2


