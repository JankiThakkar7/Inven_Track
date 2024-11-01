import sqlite3
from config.db_config import get_connection

class Product:
    def __init__(self, name, description, quantity, price, product_id=None):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        
    @staticmethod
    def add_product(name, description, quantity, price):
        """Add a new product to the database."""
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Products (name, description, quantity, price) VALUES (?,?,?,?)", (name, description, quantity, price))
                conn.commit()
                print("Product added successfully.")
            except sqlite3.Error as e:
                print("Error adding product: ",e)
            finally:
                conn.close()
                
    @staticmethod
    def get_all_products():
        """Retrieve all products from the database."""
        conn = get_connection()
        products = []
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Products")
                rows = cursor.fetchall()
                for row in rows:
                    products.append(Product(*row[1:], product_id=row[0]))
            except sqlite3.Error as e:
                print("Error retriving products: ",e)
            finally:
                conn.close()
        return products
    
    @staticmethod
    def update_product(product_id, name, description, quantity, price):
        """Update an existing product's details."""
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE Products SET name = ?, description = ?, quantity = ?, price = ? WHERE product_id = ?", (name, description, quantity, price, product_id))
                conn.commit()
                print("Product updated successfully.")
            except sqlite3.Error as e:
                print("Error updating product: ", e)
            finally:
                conn.close()
                
    @staticmethod
    def delete_product(product_id):
        """Delete a product from the database."""
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Products WHERE  product_id = ?", (product_id))
                conn.commit()
                print("Product deleted successfully.")
            except sqlite3.Error as e:
                print("Error updating product: ", e)
            finally:
                conn.close()