import sqlite3
from datetime import datetime

class DbController:
    def __init__(self,db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        
    def create_table(self, device_name, register_names):
        columns = ', '.join([f"{register} INTEGER" for register in register_names])
        query = f'''CREATE TABLE IF NOT EXISTS {device_name} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp DATETIME,
                        {columns}
                    )
                '''
        self.cursor.execute(query)
        self.connection.commit()

    def insert_data(self, device_name, data):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        columns = ', '.join(data.keys())
        values = ', '.join([str(value) for value in data.values()])
        query = f"INSERT INTO {device_name} (timestamp, {columns}) VALUES (?, {values})"
        self.cursor.execute(query, (timestamp,))
        self.connection.commit()