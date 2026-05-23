from flask import Flask, jsonify, send_file
import pandas as pd

app = Flask(__name__)

@app.route("/balance")
def balance():

    df = pd.read_csv("data/transactions.csv")

    df["signed_amount"] = df.apply(
        lambda row: row["amount"]
        if row["transaction_type"] == "income"
        else -row["amount"],
        axis=1
    )

    result = {
        "balance": float(df["signed_amount"].sum())
    }

    return jsonify(result)

@app.route("/csv")
def csv_file():
    return send_file("data/transactions.csv")

@app.route("/plot")
def plot_file():
    return send_file("exports/balance.png")

#6