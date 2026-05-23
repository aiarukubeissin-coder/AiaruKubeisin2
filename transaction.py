from dataclasses import dataclass

@dataclass
class Transaction:
    amount: float
    category: str
    transaction_type: str
    week: int

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "transaction_type": self.transaction_type,
            "week": self.week
        }
#1