
expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},
    {"description": "Taxi", "category": "Transport", "amount": 120},
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]


def add_expense(expenses):
    description = input("Enter expense description: ")
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))

    if description == "" or category == "":
        print("Description and category cannot be empty.")
    elif amount <= 0:
        print("Amount must be greater than zero.")
    else:
        expenses.append({
            "description": description,
            "category": category,
            "amount": amount
        })
        print("Expense added successfully.")


def calculate_total_expenses(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def spending_by_category(expenses):
    category_totals = []

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        found = False

        for item in category_totals:
            if item[0] == category:
                item[1] += amount
                found = True
                break

        if found == False:
            category_totals.append([category, amount])

    return category_totals


def largest_expense(expenses):
    if len(expenses) == 0:
        return None

    largest = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

    return largest


def expenses_above_threshold(expenses, threshold):
    result = []

    for expense in expenses:
        if expense["amount"] > threshold:
            result.append(expense)

    return result


def generate_report(expenses):
    if len(expenses) == 0:
        print("No expenses available.")
        return

    total = calculate_total_expenses(expenses)
    categories = spending_by_category(expenses)
    largest = largest_expense(expenses)

    print("\n========== EXPENSE REPORT ==========")
    print("Total expenses:", total)
    print("Number of expenses:", len(expenses))

    print("\n--- Spending by Category ---")

    highest_category = categories[0]

    for item in categories:
        percentage = (item[1] / total) * 100

        print("Category:", item[0])
        print("Total:", item[1])
        print("Percentage:", round(percentage, 2), "%")

        if item[1] > highest_category[1]:
            highest_category = item

    print("\nHighest spending category:", highest_category[0])
    print("Category total:", highest_category[1])

    print("\n--- Largest Expense ---")
    print("Description:", largest["description"])
    print("Category:", largest["category"])
    print("Amount:", largest["amount"])

    print("====================================")


while True:
    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add an expense")
    print("2. Calculate total expenses")
    print("3. Spending by category")
    print("4. Find the largest expense")
    print("5. Find expenses above a threshold")
    print("6. Generate spending report")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        print("Total expenses:", calculate_total_expenses(expenses))

    elif choice == "3":
        categories = spending_by_category(expenses)

        for item in categories:
            print("Category:", item[0], "| Total:", item[1])

    elif choice == "4":
        largest = largest_expense(expenses)

        if largest == None:
            print("No expenses available.")
        else:
            print("Description:", largest["description"])
            print("Category:", largest["category"])
            print("Amount:", largest["amount"])

    elif choice == "5":
        threshold = float(input("Enter threshold amount: "))
        result = expenses_above_threshold(expenses, threshold)

        if len(result) == 0:
            print("No expenses above the threshold.")
        else:
            for expense in result:
                print(
                    "Description:", expense["description"],
                    "| Category:", expense["category"],
                    "| Amount:", expense["amount"]
                )

    elif choice == "6":
        generate_report(expenses)

    elif choice == "0":
        print("Thank you for using the Expense Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")
