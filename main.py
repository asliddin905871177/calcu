
import  tkinter as tk
from tkinter import messagebox

# Funksiya: natijani hisoblash
def calculate():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Funksiya: ekranga kiritish
def add_to_expression(value):
    entry_field.insert(tk.END, value)

# Funksiya: natijani tozalash
def clear():
    entry_field.delete(0, tk.END)

# Funksiya: sin, cos, tan hisoblash
def calculate_trig(function):
    try:
        value = float(entry_field.get())
        if function == 'sin':
            result = math.sin(math.radians(value))
        elif function == 'cos':
            result = math.cos(math.radians(value))
        elif function == 'tan':
            result = math.tan(math.radians(value))
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Oyna yaratish
root = tk.Tk()
root.title("Calculator with Trigonometry")

# Matn kiritish maydoni
entry_field = tk.Entry(root, width=25, font=('Arial', 24), borderwidth=2, relief="solid")
entry_field.grid(row=0, column=0, columnspan=4)

# Tugmalar
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('tan', 5, 3)
]

# Tugmalarni yaratish
for (text, row, col) in buttons:
    if text in ['sin', 'cos', 'tan']:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: calculate_trig(t)).grid(row=row, column=col)
    elif text == '=':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=calculate).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: add_to_expression(t)).grid(row=row, column=col)

# Dasturni ishga tushirish
root.mainloop()