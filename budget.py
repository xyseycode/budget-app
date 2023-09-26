class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    title_line = self.name.center(30, "*") + '\n'
    transaction_lines = title_line
    for transaction in self.ledger:
      transaction_lines += f"{transaction['description']:.23}".ljust(
          23) + f"{transaction['amount']:.2f}".rjust(7) + '\n'
    transaction_lines += f"Total: {self.get_balance():.2f}"

    return transaction_lines

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def get_balance(self):
    balance = 0

    for transaction in self.ledger:
      balance += transaction["amount"]

    return balance

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": amount * -1, "description": description})
      return True

    return False

  def transfer(self, amount, category):
    if self.withdraw(amount, f"Transfer to {category.name}"):
      category.deposit(amount, f"Transfer from {self.name}")
      return True

    return False


def create_spend_chart(categories):
  line_1 = "Percentage spent by category"
