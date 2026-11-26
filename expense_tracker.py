"""Expense Tracker - TP3: fusion des branches et Pull Requests.

Les dépenses sont conservées en mémoire pendant l'exécution du programme.
"""

expenses = []


def add_expense():
    """Ajoute une dépense à la liste."""
    name = input("Expense name: ").strip()
    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    expenses.append({"name": name, "amount": amount})
    print("Expense added successfully.")


def show_expenses():
    """Affiche toutes les dépenses."""
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== EXPENSES =====")
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['name']} : {expense['amount']:.2f}")


def show_total():
    """Affiche le montant total des dépenses."""
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total: {total:.2f}")


def delete_expense():
    """Supprime une dépense en utilisant son numéro."""
    if not expenses:
        print("No expenses to delete.")
        return

    show_expenses()
    try:
        number = int(input("Enter the expense number to delete: "))
        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    deleted = expenses.pop(number - 1)
    print(f"{deleted['name']} deleted successfully.")


def show_average():
    """Affiche la moyenne des dépenses."""
    if not expenses:
        print("No expenses available to calculate the average.")
        return

    average = sum(expense["amount"] for expense in expenses) / len(expenses)
    print(f"Average: {average:.2f}")


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Exit")
        print("5. Delete an expense")
        print("6. Show average")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Goodbye!")
            break
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            show_average()
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
