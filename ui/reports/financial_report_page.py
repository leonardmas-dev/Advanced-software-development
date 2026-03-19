import tkinter as tk

class FinancialReportPage(tk.Frame):
    def __init__(self, parent, main_window):
        super().__init__(parent)

        tk.Label(self, text="Financial Report Page", font=("Arial", 18)).pack(pady=40)