import sqlite3

def create_db():
    # Connect to the SQLite database (creates it if it doesn't exist)
    connection = sqlite3.connect('expenses.db')

    # Create a cursor to execute SQL commands
    cursor = connection.cursor()

    # Create the expenses table if it doesn't already exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        amount REAL,
        category TEXT
    )
    ''')

    # Save the changes to the database
    connection.commit()

    # Close the database connection
    connection.close()

def main():
    # Keep displaying the menu until the user chooses to exit
    while True:

        print("\n================== Expense Tracker ==================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. View Total Spending")
        print("7. Exit")

        # Handle invalid input (non-numeric values)
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        # Call the appropriate function based on the user's choice
        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            search_expense()

        elif choice == 4:
            update_expense()

        elif choice == 5:
            delete_expense()

        elif choice == 6:
            view_total_spending()

        elif choice == 7:
            print("Thank you for using the Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")

def add_expense():

    # Get expense details from the user
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    # Connect to the database
    connection = sqlite3.connect('expenses.db')
    cursor = connection.cursor()

    # Insert the new expense into the database
    cursor.execute(
        '''INSERT INTO expenses (description, amount, category)
        VALUES (?, ?, ?)''',
        (description, amount, category)
    )

    # Save the changes
    connection.commit()

    # Close the connection
    connection.close()

    print("Successfully added your expense to the database.")

def view_expenses():

    # Connect to the database
    connection = sqlite3.connect('expenses.db')
    cursor = connection.cursor()

    # Retrieve all expenses
    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    # Display all expenses or notify the user if none exist
    if not expenses:
        print("No expenses were added to the database.")
    else:
        for expense in expenses:
            print(f"ID: {expense[0]}")
            print(f"Description: {expense[1]}")
            print(f"Amount: R{expense[2]:.2f}")
            print(f"Category: {expense[3]}")
            print("-" * 30)

    # Close the connection
    connection.close()

def search_expense():

    # Connect to the database
    connection = sqlite3.connect('expenses.db')
    cursor = connection.cursor()

    # Ask the user which category to search for
    category = input("Search expense category: ")

    # Search for all expenses in the selected category
    cursor.execute(
        "SELECT * FROM expenses WHERE category = ?",
        (category,)
    )

    expenses = cursor.fetchall()

    # Display the matching expenses
    if not expenses:
        print("No expenses found in that category.")
    else:
        for expense in expenses:
            print(f"ID: {expense[0]}")
            print(f"Description: {expense[1]}")
            print(f"Amount: R{expense[2]:.2f}")
            print(f"Category: {expense[3]}")
            print("-" * 30)

    # Close the connection
    connection.close()

def update_expense():

    # Connect to the database
    connection = sqlite3.connect('expenses.db')
    cursor = connection.cursor()

    # Get the updated expense details
    expense_id = int(input("Enter expense ID: "))
    description = input("Enter new expense description: ")
    amount = float(input("Enter new expense amount: "))
    category = input("Enter new expense category: ")

    # Update the selected expense
    cursor.execute(
        '''
        UPDATE expenses
        SET description = ?, amount = ?, category = ?
        WHERE id = ?
        ''',
        (description, amount, category, expense_id)
    )

    # Save the changes
    connection.commit()

    # Check if the expense was updated successfully
    if cursor.rowcount > 0:
        print("Expense updated successfully!")
    else:
        print("Expense not found.")

    # Close the connection
    connection.close()

def delete_expense():

    # Connect to the database
    connection = sqlite3.connect('expenses.db')
    cursor = connection.cursor()

    # Ask the user which expense to delete
    expense_id = int(input("Enter expense ID: "))

    # Delete the selected expense
    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    # Save the changes
    connection.commit()

    # Check whether the expense was deleted
    if cursor.rowcount > 0:
        print("Expense deleted successfully!")
    else:
        print("Expense not found.")

    # Close the connection
    connection.close()

def view_total_spending():

    # Connect to the database
    connection = sqlite3.connect('expenses.db')
    cursor = connection.cursor()

    # Calculate the total amount spent
    cursor.execute("SELECT SUM(amount) FROM expenses")

    total_spending = cursor.fetchone()

    # Display the total spending
    if total_spending[0] is None:
        print("No expenses found.")
    else:
        print(f"Total Spending: R{total_spending[0]:.2f}")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    create_db()
    main()


    
     
