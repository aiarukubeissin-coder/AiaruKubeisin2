from transaction import Transaction

class FamilyBudget:

    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        balance = 0

        for t in self.transactions:
            if t.transaction_type == "income":
                balance += t.amount
            else:
                balance -= t.amount

        return balance

    def get_all_transactions(self):
        return self.transactions
#2