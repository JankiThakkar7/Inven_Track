import tkinter as tk
from config.db_config import initialize_database
from views.main_view import MainView

def start_app():
    root = tk.Tk()
    root.title("Inventory Management System")
    root.geometry("800x600")

    try:
        logo_path = "assets/images/logo.png"
        root.iconphoto(False, tk.PhotoImage(file=logo_path))
    except Exception as e:
        print("Error loading logo: ",e)
    
    initialize_database()

    app = MainView(root)
    app.pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    start_app()