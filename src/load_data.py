import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_data():
    db_path = BASE_DIR / "database"
    db_path.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_path / "genalysis.db")

    tables = {
        "customers":"customers.csv",
        "order_items":"order_items.csv",
        "orders":"orders.csv",
        "products_2026":"products_2026.csv",
        "reviews":"reviews.csv",
        "sellers_2026":"sellers_2026.csv"
    }

    for table_name,file in tables.items():
        df = pd.read_csv(BASE_DIR / "data" / file)
        df.to_sql(table_name,conn,if_exists="replace",index=False)
    
    conn.close()