import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

conn = sqlite3.connect(BASE_DIR / "database" / "genalysis.db")

tables = {
    "fake_dataset":"fake_dataset.csv"
}

for table_name,file in tables.items():
    df = pd.read_csv(BASE_DIR / "data" / file)
    df.to_sql(table_name,conn,if_exists="replace",index=False)

