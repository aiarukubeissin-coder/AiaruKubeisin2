import pandas as pd
import matplotlib.pyplot as plt

def analyze_budget(filename):

    df = pd.read_csv(filename)

    df["signed_amount"] = df.apply(
        lambda row: row["amount"]
        if row["transaction_type"] == "income"
        else -row["amount"],
        axis=1
    )

    balance = df["signed_amount"].sum()

    grouped = df.groupby(["week", "category"])["signed_amount"].sum()

    print("\nБаланс:")
    print(balance)

    print("\nАналитика:")
    print(grouped)

    return df

def create_balance_plot(df):

    weekly = df.groupby("week")["signed_amount"].sum()

    plt.plot(weekly.index, weekly.values)

    plt.xlabel("Week")
    plt.ylabel("Balance")
    plt.title("Family Budget Balance")

    plt.savefig("exports/balance.png")

    plt.close()
#5