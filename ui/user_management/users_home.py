import tkinter as tk

class UsersHome(tk.Frame):
    def __init__(self, parent, main_window):
        super().__init__(parent)

        tk.Label(self, text="User Management Home", font=("Arial", 18)).pack(pady=40)