import tkinter as tk
from tkinter import messagebox

# Global variable to store all employees
employees = []


def add_employee():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    department = entry_department.get()
    role = entry_role.get()
    salary = entry_salary.get()

    if not name or not age or not gender or not department or not role or not salary:
        messagebox.showerror("Error", "Please fill all the fields.")
        return

    employees.append({
        "name": name,
        "age": age,
        "gender": gender,
        "department": department,
        "role": role,
        "salary": salary
    })

    # Reset the form
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    entry_role.delete(0, tk.END)
    entry_salary.delete(0, tk.END)

    # Show success message
    messagebox.showinfo("Success", "Employee added successfully.")


# Create the main window
root = tk.Tk()
root.title("HR Management System")

# Create the form widgets
label_name = tk.Label(root, text="Name:")
label_age = tk.Label(root, text="Age:")
label_gender = tk.Label(root, text="Gender:")
label_department = tk.Label(root, text="Department:")
label_role = tk.Label(root, text="Role:")
label_salary = tk.Label(root, text="Salary:")

entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_gender = tk.Entry(root)
entry_department = tk.Entry(root)
entry_role = tk.Entry(root)
entry_salary = tk.Entry(root)

button_add = tk.Button(root, text="Add Employee", command=add_employee)

# Place the form widgets on the grid
label_name.grid(row=0, column=0)
label_age.grid(row=1, column=0)
label_gender.grid(row=2, column=0)
label_department.grid(row=3, column=0)
label_role.grid(row=4, column=0)
label_salary.grid(row=5, column=0)

entry_name.grid(row=0, column=1)
entry_age.grid(row=1, column=1)
entry_gender.grid(row=2, column=1)
entry_department.grid(row=3, column=1)
entry_role.grid(row=4, column=1)
entry_salary.grid(row=5, column=1)

button_add.grid(row=6, column=1)

# Start the main event loop
root.mainloop()
