import tkinter as tk

def on_click(button_text):
    if button_text == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculator")


entry = tk.Entry(root, width=15, font=("Helvetica", 20), bd=10, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4)


button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_index, col_index = 1, 0
for button_text in button_texts:
    if col_index == 4:
        col_index = 0
        row_index += 1

    button = tk.Button(root, text=button_text, font=("Helvetica", 20), padx=20, pady=20,
                       command=lambda text=button_text: on_click(text))
    button.grid(row=row_index, column=col_index)
    col_index += 1

root.mainloop()
