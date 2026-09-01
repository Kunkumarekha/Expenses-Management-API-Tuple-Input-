expenses = []

def insert_expense(title, category, amount, date):
    expense = (title, category, amount, date)
    expenses.append(expense)

print("Expense added successfully!")


def get_all_expenses():
    return expenses

def search_expense(name):
    for expense in expenses:
        if expense[0].lower() == name.lower():
            return expense
            return None


def delete_expense(title):

    for expense in expenses:

        if expense[0].lower() == title.lower():

            expenses.remove(expense)

            return True

    return False


def update_expense_amount(name, new_amount):
    for i in range(len(expenses)):
        expense = expenses[i]
        if expense[0].lower() == name.lower():
            expenses[i] = (expense[0],expense[1],new_amount,expense[3])

        print("Expense amount updated successfully!")
        return

print("Expense not found!")

