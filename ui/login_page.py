import tkinter as tk
from tkinter import messagebox

from database.session import get_session
from backend.auth_service import AuthService
from ui.main_window import MainWindow


class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()

        # Basic window setup
        self.title("PAMS Login")
        self.geometry("400x300")

        # Username field
        tk.Label(self, text="Username").pack(pady=(30, 5))
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        # Password field
        tk.Label(self, text="Password").pack(pady=(15, 5))
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # Login button
        tk.Button(self, text="Login", command=self.handle_login).pack(pady=25)

    def handle_login(self):
        # Get input values
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Basic validation
        if not username or not password:
            messagebox.showerror("Error", "Please enter both fields")
            return

        # Open DB session
        db = get_session()
        auth = AuthService(db)

        # Try to authenticate
        session = auth.authenticate(username, password)

        if session is None:
            messagebox.showerror("Login Failed", "Invalid username or password")
            db.close()
            return

        # Close DB session after login
        db.close()

        # Destroy login window and open main UI
        self.destroy()
        app = MainWindow(user_session=session)
        app.mainloop()