import json
import os

class Config:
    def __init__(self, dbconfig_file='config.json'):
        self.dbconfig_file = dbconfig_file
        self.load_dbconfig()
    
    def load_dbconfig(self):
        if not os.path.exists(self.dbconfig_file):
            raise FileNotFoundError(f"Database configuration file not found.")
        with open(self.dbconfig_file) as f:
            dbconfig_data = json.load(f)
            self.DB_HOST = dbconfig_data.get("DB_HOST")
            self.DB_USER = dbconfig_data.get("DB_USER")
            self.DB_PORT = dbconfig_data.get("DB_PORT")
            self.DB_PASSWORD = dbconfig_data.get("DB_PASSWORD")
            self.DB_NAME = dbconfig_data.get("DB_NAME")

config = Config()