expenses = []

try:
    with open("expenses.txt", "r") as f:
        for line in f:
            name, amount = line.strip().split(",")
            expenses.append((name, float(amount)))
except FileNotFoundError:
    pass

while True:
    print("\n1.Add Expense")
    print("2.View Expenses")
    print("3.Total Spending")
    print("4.Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append((name, amount))

        with open("expenses.txt", "a") as f:
            f.write(f"{name},{amount}\n")

        print("Expense added & saved!")

    elif choice == "2":
        print("\nExpenses:")
        for e in expenses:
            print(e[0], "-", e[1])

    elif choice == "3":
        total = sum(e[1] for e in expenses)
        print("Total spending:", total)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
