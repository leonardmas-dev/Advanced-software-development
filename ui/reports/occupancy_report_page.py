import tkinter as tk

class OccupancyReportPage(tk.Frame):
    def __init__(self, parent, main_window):
        super().__init__(parent)

        tk.Label(self, text="Occupancy Report Page", font=("Arial", 18)).pack(pady=40)