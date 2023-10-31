import tkinter as tk
from tkinter import messagebox

def create_main_window():
    window = tk.Tk()
    window.title("HR Management System")
    window.geometry("350x300")


# Labels and entries
    name_label = tk.Label(window, text="Name:")
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1)

    email_label = tk.Label(window, text="Email:")
    email_label.grid(row=1, column=0)
    email_entry = tk.Entry(window)
    email_entry.grid(row=1, column=1)

    phone_label = tk.Label(window, text="Phone:")
    phone_label.grid(row=2, column=0)
    phone_entry = tk.Entry(window)
    phone_entry.grid(row=2, column=1)

    register_date_label = tk.Label(window, text="Register Date:")
    register_date_label.grid(row=3, column=0)
    register_date_entry = tk.Entry(window)
    register_date_entry.grid(row=3, column=1)

    user_status_label = tk.Label(window, text="User Status:")
    user_status_label.grid(row=4, column=0)
    user_status_entry = tk.Entry(window)
    user_status_entry.grid(row=4, column=1)

    role_label = tk.Label(window, text="Role:")
    role_label.grid(row=5, column=0)
    role_entry = tk.Entry(window)
    role_entry.grid(row=5, column=1)

    role_label = tk.Label(window, text="Role:")

    return window

def add_employee():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    register_date = register_date_entry.get()
    user_status = user_status_entry.get()
    role = role_entry.get()

    employees.append([name, email, phone, register_date, user_status, role])

    name_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    register_date_entry.delete(0, 'end')
    user_status_entry.delete(0, 'end')
    role_entry.delete(0, 'end')

    messagebox.showinfo("Success", "Employee added successfully.")

    def export_data():
    with open("employee_data.txt", "w") as file:
        for employee in employees:
            file.write("\n".join(employee))
            file.write("\n")
    messagebox.showinfo("Success", "Employee data exported successfully.")
