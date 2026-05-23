from budget import FamilyBudget
from generator import generate_week_transactions
from storage import save_to_json, export_csv
from analytics import analyze_budget, create_balance_plot

budget = FamilyBudget()

for week in range(1, 13):

    generated = generate_week_transactions(week)

    for transaction in generated:
        budget.add_transaction(transaction)

transactions = budget.get_all_transactions()

save_to_json(transactions, "data/budget.json")

export_csv(transactions, "data/transactions.csv")

df = analyze_budget("data/transactions.csv")

create_balance_plot(df)

print("Текущий баланс:", budget.get_balance())

print("Файлдар дайын.")

from api import app

app.run(debug=True, port=5002)