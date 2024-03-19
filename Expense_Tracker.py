import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, date, amount, category):
        if date not in self.expenses:
            self.expenses[date] = []
        self.expenses[date].append({"amount": amount, "category": category})

    def view_spending_pattern(self):
        print("Spending Pattern:")
        for date, expenses in self.expenses.items():
            total_amount = sum(expense["amount"] for expense in expenses)
            print(f"{date}: Total expenses = ${total_amount}")
            for expense in expenses:
                print(f"\tCategory: {expense['category']}, Amount: ${expense['amount']}")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Spending Pattern")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue
            amount = float(input("Enter amount: $"))
            category = input("Enter category: ")
            expense_tracker.add_expense(date, amount, category)
            print("Expense added successfully!")
        elif choice == "2":
            expense_tracker.view_spending_pattern()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
