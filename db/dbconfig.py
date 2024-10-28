import json
import os


class Config:
    def __init__(self):
        self.load_dbconfig()

    def load_dbconfig(self):
        config_file_path = os.path.join(os.path.dirname(__file__), 'config.json')
        if not os.path.exists(config_file_path):
            raise FileNotFoundError(f"Database configuration file not found.")
        with open(config_file_path) as f:
            dbconfig_data = json.load(f)
            self.DB_HOST = dbconfig_data.get("DB_HOST")
            self.DB_USER = dbconfig_data.get("DB_USER")
            self.DB_PORT = dbconfig_data.get("DB_PORT")
            self.DB_PASSWORD = dbconfig_data.get("DB_PASSWORD")
            self.DB_NAME = dbconfig_data.get("DB_NAME")

config = Config()