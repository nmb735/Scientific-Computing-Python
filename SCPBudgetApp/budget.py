class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        # Record a deposit in the ledger.
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        # Check if there are sufficient funds for a transaction.
        balance = sum(item["amount"] for item in self.ledger)
        return balance >= amount

    def withdraw(self, amount, description=""):
        # Record a withdrawal in the ledger.
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        # Calculate and return the account balance.
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget):
        # Transfer funds to another budget category.
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + budget.name)
            budget.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def __str__(self):
        # String representation of the category.
        aster = "*" * ((30 - len(self.name)) // 2)
        firstline = aster + self.name + aster + "\n"
        transactions = ""
        for transaction in self.ledger:
            concept = transaction["description"][:23]
            concept = concept.ljust(23)  # Left-align concept
            money = "{:.2f}".format(transaction["amount"])
            money = money.rjust(30 - len(concept))  # Right-align money
            transactions += concept + money + "\n"
        total = "Total: {:.2f}".format(self.get_balance())
        return firstline + transactions + total


def create_spend_chart(categories):
    # Create the title of the chart
    chart_title = "Percentage spent by category\n"

    # Calculate total spending for each category and overall
    spendings = [sum(item["amount"] for item in category.ledger if item["amount"] < 0) for category in categories]
    total_spent = sum(spendings)

    # Calculate spending percentages
    percentages = [(spending / total_spent) * 100 for spending in spendings]

    # Build the chart line by line
    chart_line = ""
    for i in range(100, -1, -10):
        chart_line += str(i).rjust(3) + "| "
        for percentage in percentages:
            chart_line += "o  " if percentage >= i else "   "
        chart_line += "\n"

    # Create the horizontal line
    dash = "    " + "-" * (3 * len(categories)) + "-\n"

    # Calculate the maximum name length
    max_name_length = max(len(category.name) for category in categories)

    # Build the names row by row
    names = ""
    for i in range(max_name_length):
        names += "     "
        for category in categories:
            if i < len(category.name):
                names += category.name[i] + "  "
            else:
                names += "   "
        names += "\n"

    # Combine all parts to form the chart
    barchart = (chart_title + chart_line + dash + names).rstrip() + "  "
    return barchart


# User testing - Formatting:
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(1000, "initial deposit")
entertainment.deposit(2000, "initial deposit")
business.deposit(3000, "initial deposit")

food.withdraw(10.15, "groceries")
entertainment.withdraw(15.89, "restaurant and more food")
business.transfer(50, food)

print(create_spend_chart([food, entertainment, business]))
