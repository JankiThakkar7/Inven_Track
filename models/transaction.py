import sqlite3
from config.db_config import get_connection
from models.product import Product

class Transaction:
    def __init__(self, product_id, quantity, total_price, transaction_id = None, transaction_date=None):
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price
        self.transaction_date = transaction_date
        
    @staticmethod
    def add_transaction(product_id, quantity):
        """Add a transaction and update product quantity in inventory."""
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                product = Product.get_all_products()
                selected_product = next((p for p in product if p.product_id == product_id), None)
                if selected_product and selected_product.quantity >= quantity:
                    total_price = quantity * selected_product.price
                    cursor.execute("INSERT INTO Transactions (product_id, quantity, total_price) VALUES (?,?,?)", (product_id, quantity, total_price))
                    new_quantity = selected_product.quantity - quantity
                    Product.update_product(product_id, selected_product.name, selected_product.description, new_quantity, selected_product.price)
                    conn.commit()
                    print("Transaction added successfully.")
                else:
                    print("Insufficent stock for the transaction.")
            except sqlite3.Error as e:
                print("Error adding transaction: ", e)
            finally:
                conn.close()
    
    @staticmethod
    def get_all_transaction():
        """Retrieve all transactions from the database."""
        conn = get_connection()
        transactions = []
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Transactions")
                rows = cursor.fetchall()
                for row in rows:
                    transactions.append(Transaction(*row[1:], transaction_id=row[0], transaction_date=row[4]))
            except sqlite3.Error as e:
                print("Error retrieving transactions: ", e)
            finally:
                conn.close()
        return transactions
    