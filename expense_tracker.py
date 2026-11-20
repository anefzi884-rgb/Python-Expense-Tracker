

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append({"name": name, "amount": amount})
    print("Expense added successfully!")

def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - {expense['amount']:.2f}")

def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: {total:.2f}")

def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    show_expenses()

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            print(f"{deleted['name']} deleted successfully!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add an expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Exit")
    print("5. Delete an expense")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        break
    elif choice == "5":
        delete_expense()
    else:
        print("Invalid choice.")
