import tkinter as tk

class EditUserPage(tk.Frame):
    def __init__(self, parent, main_window):
        super().__init__(parent)

        tk.Label(self, text="Edit User Page", font=("Arial", 18)).pack(pady=40)