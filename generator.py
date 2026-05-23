import random
from transaction import Transaction
random.seed(42)

categories_income = ["salary", "bonus"]
categories_expense = ["food", "transport", "shopping"]

def generate_week_transactions(week):

    transactions = []

    for _ in range(5):

        if random.choice([True, False]):
            t = Transaction(
                amount=random.randint(50000, 200000),
                category=random.choice(categories_income),
                transaction_type="income",
                week=week
            )

        else:
            t = Transaction(
                amount=random.randint(1000, 30000),
                category=random.choice(categories_expense),
                transaction_type="expense",
                week=week
            )

        transactions.append(t)

    return transactions
#3