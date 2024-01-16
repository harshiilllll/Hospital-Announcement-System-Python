import tkinter as tk
from tkinter import ttk
from functools import partial
from gtts import gTTS
import os

def announce_code(code, department_var, floor_var, is_deactivated_var):
    department = department_var.get()
    floor = floor_var.get()
    is_deactivated = is_deactivated_var.get()

    # Check if both department and floor are selected
    if not department or not floor:
        show_error("Please select both department and floor.")
        return

    message = f"Attention please, code {code}, {department} department, {floor} Floor"

    # Append "Is Deactivated" if the checkbox is checked
    if is_deactivated:
        message += " Is Deactivated"

    tts = gTTS(text=message, lang='en', slow=False)
    tts.save("announcement.mp3")

    os.system("start announcement.mp3")

def show_error(message):
    error_label.config(text=message)

# GUI setup
root = tk.Tk()
root.title("Hospital Announcement System")
root.geometry("400x650")

# Department dropdown
departments = ["Cardiology", "Emergency", "Orthopedics", "Radiology", "Surgery", "Other"]
department_label = tk.Label(root, text="Select Department:", font=("Arial", 14))
department_label.pack()

department_var = tk.StringVar()
department_dropdown = ttk.Combobox(root, textvariable=department_var, values=departments, font=("Arial", 12), width=20)
department_dropdown.pack(pady=5)

# Floor dropdown
floors = ["Basement 1", "Basement 2", "Ground", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th"]
floor_label = tk.Label(root, text="Select Floor:", font=("Arial", 14))
floor_label.pack()

floor_var = tk.StringVar()
floor_dropdown = ttk.Combobox(root, textvariable=floor_var, values=floors, font=("Arial", 12), width=20)
floor_dropdown.pack(pady=5)

# Is Deactivated checkbox
is_deactivated_var = tk.BooleanVar()
is_deactivated_checkbox = tk.Checkbutton(root, text="Is Deactivated?", variable=is_deactivated_var, font=("Arial", 14))
is_deactivated_checkbox.pack(pady=5)

# Error label
error_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
error_label.pack(pady=5)

# Code buttons
codes = ["Blue", "Violet", "Orange", "Red", "Black"]
for code in codes:
    button = tk.Button(root, text=f"Code {code}", command=partial(announce_code, code, department_var, floor_var, is_deactivated_var),
                       font=("Arial", 14), width=20, height=2)

    # Set button colors according to codes
    if code == "Blue":
        button.configure(bg="blue", fg="white")
    elif code == "Red":
        button.configure(bg="red", fg="white")
    elif code == "Violet":
        button.configure(bg="purple", fg="white")
    elif code == "Orange":
        button.configure(bg="orange", fg="white")
    elif code == "Black":
        button.configure(bg="black", fg="white")

    button.pack(pady=10)

root.mainloop()
