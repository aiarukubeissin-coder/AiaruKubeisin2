from fastapi import FastAPI
from fastapi.responses import FileResponse
import pandas as pd
import uvicorn

app = FastAPI()

@app.get("/balance")
def get_balance():

    df = pd.read_csv("data/transactions.csv")

    df["signed_amount"] = df.apply(
        lambda row:
        row["amount"]
        if row["transaction_type"] == "income"
        else -row["amount"],
        axis=1
    )

    balance = float(df["signed_amount"].sum())

    return {
        "balance": balance
    }

@app.get("/csv")
def get_csv():
    return FileResponse("data/transactions.csv")

@app.get("/plot")
def get_plot():
    return FileResponse("exports/balance.png")

#6