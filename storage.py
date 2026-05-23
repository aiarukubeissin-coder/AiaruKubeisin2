import json
import pandas as pd

def save_to_json(transactions, filename):

    data = [t.to_dict() for t in transactions]

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def export_csv(transactions, filename):

    data = [t.to_dict() for t in transactions]

    df = pd.DataFrame(data)

    df.to_csv(filename, index=False)
#4