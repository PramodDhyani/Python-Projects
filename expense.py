import csv

class ExpenseTracker:
    def __init__(self, file_name="expenses.csv"):
        self.file_name = file_name

    def add_expense(self):
        """Add a new expense to the file."""
        print("---- Add Expense ----")
        date = input("Enter the date (YYYY-MM-DD): ").strip()
        description = input("Enter the description: ").strip()
        amount = input("Enter the amount: ").strip()

        # Save the expense to the file
        with open(self.file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, description, amount])
        print("Expense added successfully!")

    def view_expenses(self):
        """View all expenses from the file."""
        print("---- View All Expenses ----")
        try:
            with open(self.file_name, "r") as file:
                reader = csv.reader(file)
                expenses = list(reader)  # Read all rows into a list
                
                if not expenses:
                    print("No expenses found.")
                    return

                # Display all expenses
                for row in expenses:
                    print(f"Date: {row[0]}, Description: {row[1]}, Amount: {row[2]}")
        except FileNotFoundError:
            print("No expense file found. Start adding some expenses!")

    def search_expenses_by_date(self):
        """Search for expenses by a specific date."""
        print("---- Search Expenses by Date ----")
        search_date = input("Enter the date (YYYY-MM-DD): ").strip()

        try:
            with open(self.file_name, "r") as file:
                reader = csv.reader(file)
                found = False

                for row in reader:
                    if row[0] == search_date:
                        print(f"Date: {row[0]}, Description: {row[1]}, Amount: {row[2]}")
                        found = True

                if not found:
                    print(f"No expenses found for the date: {search_date}")
        except FileNotFoundError:
            print("No expense file found. Start adding some expenses!")

    def menu(self):
        """Display the menu and handle user choices."""
        while True:
            print("\n---- Expense Tracker Menu ----")
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. Search Expenses by Date")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.search_expenses_by_date()
            elif choice == "4":
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")


# Run the program
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.menu()
