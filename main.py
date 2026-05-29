from src.export_queries import export_queries
from src.load_data import load_data

def main():
    load_data()
    export_queries()

if __name__ == "__main__":
    main()