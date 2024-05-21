
import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    email = entry_email.get()   
    
    
    if not username or not password or not confirm_password or not email:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return
    
    
    messagebox.showinfo("Success", "Registration Successful!")
    
    
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_confirm_password.delete(0, tk.END)
    entry_email.delete(0, tk.END)


root = tk.Tk()
root.title("Registration Form")


label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")  
entry_password.pack()

label_confirm_password = tk.Label(root, text="Confirm Password:")
label_confirm_password.pack()
entry_confirm_password = tk.Entry(root, show="*")  # Show '*' for password
entry_confirm_password.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()


button_register = tk.Button(root, text="Register", command=register)
button_register.pack()


root.mainloop()
