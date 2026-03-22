import sys
import os
# Ensures database.models can be read by this file
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import tkinter as tk
from tkinter import ttk, messagebox
from database.models import Tenant
from database.session import get_session

#automatically close the session by using with
def fetch_tenants():
    with get_session() as session:
        tenants = session.query(Tenant).all()
    return tenants


root = tk.Tk()
root.title("Tenant List")
root.geometry("1200x400")

tk.Label(root, text="Tenant Information")

# Displaying the tenant data
columns = ("Tenant ID", "First Name", "Last Name", "Phone", "Email", "Apartment")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(fill="both", expand=True)

# If content goes off screen scroll bar allows to view more
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Fetch tenants and insert into treeview
for tenant in fetch_tenants():
    tree.insert(
        "",
        "end",
        values=(
            tenant.tenant_id,
            tenant.first_name,
            tenant.last_name,
            tenant.phone,
            tenant.email,
            tenant.location_id 
        )
    )

root.mainloop()