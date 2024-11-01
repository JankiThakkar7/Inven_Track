from models.product import Product

class Inventory:
    
    @staticmethod
    def add_new_product(name, description, quantity, price):
        """Add a new product to the inventory."""
        Product.add_product(name, description, quantity, price)
        
    @staticmethod
    def update_product(product_id, name, description, quantity, price):
        """Update an existing product in the inventory."""
        Product.update_product(product_id, name, description, quantity, price)
        
    @staticmethod
    def delete_product(product_id):
        """Remove a product from the inventory."""
        Product.delete_product(product_id)
        
    @staticmethod
    def get_all_produts():
        """Get all products in the inventory."""
        return Product.get_all_products()
    
    @staticmethod
    def check_stock_levels(threshold = 5):
        """Get a list of products with quantity below the threshold."""
        low_stock_products = []
        products = Product.get_all_products()
        for product in products:
            if product.quantity < threshold:
                low_stock_products.append(product)
        return low_stock_products
    
    @staticmethod
    def get_inventory_summary():
        """Provide a summary of the inventory (total products, total stock value)."""
        total_quantity = 0
        total_value = 0.0
        products = Product.get_all_products()
        for product in products:
            total_quantity += product.quantity
            total_value += product.quantity * product.price
        return {
            "total_products": len(products),
            "total_quantity": total_quantity,
            "total_value": total_value
        }