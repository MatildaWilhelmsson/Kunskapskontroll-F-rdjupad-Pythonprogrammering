
import logging
import sqlite3

class ToSQL:
    """A class that takes a DataFrame as input and exports and saves it as a table in a SQL database."""
    
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
    
    def sql_saver(self, df):  
        self.logger.info("Creating and connecting to SQL-database...")
        con = sqlite3.connect("Kommunalskatt.db")
        self.logger.info("Database connected.")
        self.logger.info("Turning DataFrame into SQL-table and sending to database...")
        print(df.to_sql("Kommunalskatt_2024", con, if_exists="replace"))
        return df.to_sql("Kommunalskatt_2024", con, if_exists="replace")
