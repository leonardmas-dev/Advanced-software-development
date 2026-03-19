from ui.login_page import LoginPage
from database.database_manager import initialize_database

def main():
    # Ensure DB is ready
    initialize_database()
    # Start login screen
    login = LoginPage()
    login.mainloop()

if __name__ == "__main__":
    main()