import tkinter as tk
from views.product_view import ProductView
from views.sales_view import SalesView
from views.reports_view import ReportsView

class MainView(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        self.title_label = tk.Label(self, text="Inventory Management System", font=("Arial", 18))
        self.title_label.pack(pady=20)
        
        self.product_botton = tk.Button(self, text="Product Management", command=self.open_product_view)
        self.product_botton.pack(pady=10, ipadx=10, ipady=5)
        
        self.sales_button = tk.Button(self, text="Sales", command=self.open_sales_view)
        self.sales_button.pack(pady=10, ipadx=10, ipady=5)
        
        self.reports_button = tk.Button(self, text="Reports", command=self.open_reports_view)
        self.reports_button.pack(pady=10, ipadx=10, ipady=5)

    def open_product_view(self):
        """Open the Product Management View"""
        product_view = ProductView(self.master)
        product_view.pack(fill="both", expand=True)
        self.pack_forget()
        
    def open_sales_view(self):
        """Open the Sales View."""
        sales_view = SalesView(self.master)
        sales_view.pack(fill="both", expand=True)
        self.pack_forget()
    
    def open_reports_view(self):
        """Open the Reports View."""
        reports_view = ReportsView(self.master)
        reports_view.pack(fill="both", expand=True)
        self.pack_forget()