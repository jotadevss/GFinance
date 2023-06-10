import tkinter as tk
from Source.Controller.controller import *
from Source.View.Components.backButton import *

def interface_transaction():
    trUI = tk.Toplevel()

    def clear():
        # Function to clear input fields
        title_input.delete(0, "end")
        value_input.delete(0, "end")
        category_input.delete(0, "end")

    trUI.title("Adicionar Transação")
    trUI.geometry("800x800")
    trUI.config(padx=10, pady=100)
    trUI.resizable(width=False, height=False)

    header_label = tk.Label(trUI, text="Preencha todos os campos para adicionar a sua transação.", font=("Calibri", 16, "italic"))
    header_label.pack()

    title_label = tk.Label(trUI, text="Título", font=("Calibri", 14))
    title_label.pack(pady=10)
    title_input = tk.Entry(trUI, text="title", width=30, font=("Calibri", 12))
    title_input.pack(pady=5)

    value_label = tk.Label(trUI, text="Valor", font=("Calibri", 14))
    value_label.pack(pady=10)
    value_input = tk.Entry(trUI, text="value", width=30, font=("Calibri", 12))
    value_input.pack(pady=5)

    category_label = tk.Label(trUI, text="Tipologia", font=("Calibri", 14))
    category_label.pack(pady=10)
    category_input = tk.Entry(trUI, text="tipologia", width=30, font=("Calibri", 12))
    category_input.pack(pady=5)

    atentation_label = tk.Label(trUI, text="[DICA]\n\nNo campo TIPOLOGIA, coloque a referência que caracterize essa transação\n Por exemplo: Receita, Despesas, Gastos, Ganhos, e etc.", font=("Calibri", 12, "italic"))
    atentation_label.pack()

    add_transaction_btn = tk.Button(
        trUI,
        text="Adicionar Transação",
        width=36,
        pady=15,
        bg="#5f9ea0",
        fg="white",
        font=("Calibri", 12, "bold"),
        command=lambda: add_transaction(title=title_input.get(), value=value_input.get(), category=category_input.get(), func_clear=clear)
    )
    add_transaction_btn.pack(pady=40)

    back_button(trUI, trUI.destroy)
