class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}"[:7].rjust(7)
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    spendings = []
    category_names = []

    
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spendings.append(total)
        category_names.append(category.name)

    
    total_spent = sum(spendings)
    percentages = [int((s / total_spent) * 10) * 10 for s in spendings]

   
    chart = ""
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    
    max_len = max(len(name) for name in category_names)
    for i in range(max_len):
        chart += "    "
        for name in category_names:
            letter = name[i] if i < len(name) else " "
            chart += f" {letter} "
        chart += " \n"

    return title + chart.rstrip("\n")
