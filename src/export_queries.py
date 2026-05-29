import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def export_queries():
    output = BASE_DIR / "output"
    output.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(BASE_DIR / "database" / "genalysis.db")

    for file in (BASE_DIR / "sql_queries").glob("*"):

        with open(file) as f:
            sql = f.read()

        df = pd.read_sql_query(sql, conn)
        df.to_csv(output / f"{file.stem}.csv", index=False) 
    
    conn.close()