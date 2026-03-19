import tkinter as tk

class ReportsHome(tk.Frame):
    def __init__(self, parent, main_window):
        super().__init__(parent)

        tk.Label(self, text="Reports Home", font=("Arial", 18)).pack(pady=40)