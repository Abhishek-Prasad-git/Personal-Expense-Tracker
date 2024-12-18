def start_expense_tracker():
    print("Welcome to the Personal Expense Tracker!")
    expenses = {}  # Dictionary to store expenses by category
    load_data(expenses)  # Load saved data if any
    run_expense_tracker(expenses)

def input_expense(expenses):
    category = input("Enter the expense category (e.g., Food, Travel): ").strip()
    amount = float(input("Enter the expense amount: ").strip())
    
    if category in expenses:
        expenses[category].append(amount)
    else:
        expenses[category] = [amount]
    
    print(f"Expense added: {category} - {amount}")

def view_total(expenses):
    print("\nExpense Summary:")
    for category, amounts in expenses.items():
        total = sum(amounts)
        print(f"{category}: {total}")

def run_expense_tracker(expenses):
    while True:
        print("\nOptions: \n1. Add Expense \n2. View Total \n3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            input_expense(expenses)
        elif choice == "2":
            view_total(expenses)
        elif choice == "3":
            save_data(expenses)
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def save_data(expenses):
    with open("expenses.txt", "w") as file:
        for category, amounts in expenses.items():
            file.write(f"{category}: {', '.join(map(str, amounts))}\n")
    print("Expenses saved to file.")

def load_data(expenses):
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                category, amounts = line.strip().split(": ")
                expenses[category] = list(map(float, amounts.split(", ")))
    except FileNotFoundError:
        print("No previous data found.")

# Start the program
start_expense_tracker()
