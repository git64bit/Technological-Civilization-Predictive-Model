import os
import sqlite3
import configparser

def create_metadata_table(database_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    # Create the metadata table
    cursor.execute('''CREATE TABLE IF NOT EXISTS metadata (
                        id INTEGER PRIMARY KEY,
                        table_name TEXT NOT NULL,
                        field_name TEXT NOT NULL,
                        data_type TEXT NOT NULL,
                        description TEXT
                    )''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Read the database path from the config.ini file
    config = configparser.ConfigParser()
    config.read('config.ini')
    database_path = config['DATABASE']['path']
    
    # Create the metadata table
    create_metadata_table(database_path)
    print("Metadata table created successfully.")
