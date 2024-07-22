import tkinter as tk


def button_click(symbol):
    current = display.get()
    if symbol == '=':
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Erro")
    elif symbol == 'C':
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, symbol)


root = tk.Tk()
root.title("Calculadora")

# Cria o campo de entrada (display)
display = tk.Entry(root, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definindo os botões
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

# Criando e posicionando os botões na calculadora
for (symbol, row, column) in buttons:
    btn = tk.Button(root, text=symbol, padx=20, pady=20,
                    command=lambda sym=symbol: button_click(sym))
    btn.grid(row=row, column=column, padx=5, pady=5)

root.mainloop()
