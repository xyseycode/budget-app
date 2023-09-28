class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    transaction_lines = self.name.center(30, "*") + '\n'
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
  len_categories = len(categories)
  len_name_categories = []
  # check the number of categories
  if len_categories > 4:
    return "Error: categories should not exceed 4!"
  # store the total withdrawals from the categories in a list
  total_expenses = []
  for category in categories:
    #store the length of each category name to be use later
    len_name_categories.append(len(category.name))
    total_withdrawals = {category.name: 0}
    #sum all withdrawals in the category then store it in total_expenses
    for withdrawals in category.ledger:
      if withdrawals["amount"] < 0:
        total_withdrawals[category.name] += withdrawals["amount"]
    total_expenses.append(total_withdrawals[category.name])
  
  #line 1 of the chart 
  line_1 = "Percentage spent by category\n"

  # generate bar chart in each category and store them in category_line_list
  category_line_list = []
  for c in range(len_categories):
    percentage = int(((total_expenses[c] / sum(total_expenses) * 100)) // 10)
    line = []
    perc = 11 - (percentage + 1)
    for i in range(11):
      if i < perc:
        line.append(" ")
      else:
        line.append("o")
    category_line_list.append(line)

  label_line = []
  for i in range(100, -1, -10):
    label_line.append(str(i).rjust(3) + "|")

  # for bar chart with labels
  line_2 = ""
  for i in range(11):
    line_2 += label_line[i]
    for line in category_line_list:
      line_2 += " " + line[i] + " "
    line_2 += " \n"
    
  #generate dash lines
  line_3 = "    " + "-" * (len_categories * 3) + '-\n'

  # for the category names
  line_4 = ""
  max_len_categories = max(len_name_categories)
  for i in range(max_len_categories):
    line_4 += "    "
    for category in categories:
      if i < len(category.name):
        line_4 += category.name[i].center(3)
      else:
        line_4 += " ".center(3)
    line_4 += ' \n'

  return line_1 + line_2 + line_3 + line_4[:-1]
