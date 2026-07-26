import tkinter as tk

def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x380")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text == "=":
        cmd = calculate
    else:
        cmd = lambda t=text: press(t)

    tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
              command=cmd).grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text="Clear", width=24, font=("Arial", 12),
          command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()
