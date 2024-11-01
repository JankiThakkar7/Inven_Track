import sqlite3
import os

DB_PATH = os.path.join("data", "inventory.db")

def get_connection():
    """Establish a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print("Error connecting to database: ", e)
        return None
    
def initialize_database():
    """Initialize the database by creating required tables."""
    conn = get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS Products ( product_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT, quantity INTEGER NOT NULL DEFAULT 0, price REAL NOT NULL)")

            cursor.execute("CREATE TABLE IF NOT EXISTS Transactions ( transaction_id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER, quantity INTEGER NOT NULL, total_price REAL NOT NULL DEFAULT 0, transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (product_id) REFERENCES Products(product_id))")

            conn.commit()
            print("Database initialized successfully.")
        
        except sqlite3.Error as e:
            print("Error initializing database: ", e)
        
        finally:
            conn.close()
    
    else:
        print("Failed to connect to the database.")


