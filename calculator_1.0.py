import tkinter as tk

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("550x450")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(expand=True)

def click(value):
    if value == "C":
        display.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, value)


def button_(value):
    return tk.Button(
        frame,
        text=value,
        command=lambda: click(value),
        width=6,
        height=3
    )

for col in range(4):
    frame.grid_columnconfigure(col, weight=1)

display = tk.Entry(
    frame,
    width=20,
    font=("Arial", 24),
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")



buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row, values in enumerate(buttons, start=1):
    for col, value in enumerate(values):
        button_(value).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()