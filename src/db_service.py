import sqlite3
import pandas as pd
import os

class DatabaseHandler:
    def __init__(self, db_path):
        self.db_path = db_path

    def save_to_db(self, df):
        """Saves DataFrame to SQLite database."""
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Database file not found at {self.db_path}")
        conn = sqlite3.connect(self.db_path)

        df.to_sql('image_data', conn, if_exists='replace', index=False)
        conn.close()


    def execute_query(self, query: str) -> pd.DataFrame:
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Database file not found at {self.db_path}")
        conn = sqlite3.connect(self.db_path)
        try:
            return pd.read_sql_query(query, conn)
        finally:
            conn.close()