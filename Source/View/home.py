import tkinter as tk
from Source.View.transaction import *
from Source.View.exported import *
from Source.View.quotation import *
from Source.Controller.controller import *


def interface_home(self_tkinter):
    win = self_tkinter
    win.title("Gerenciador Financeiro")
    win.geometry("800x800")
    win.config(padx=10, pady=100)
    win.resizable(width=False, height=False)

    welcome_container = tk.Frame(win, padx=36, pady=20)
    welcome_container.pack()
    welcome_label = tk.Label(welcome_container, text="Bem-Vindo ao GFinance\nGerenciador Financeiro", font=("Calibri", 16, "italic"))
    welcome_label.pack()

    add_transaction_container = tk.Frame(win, padx=36, pady=5)
    add_transaction_container.pack()
    add_transaction_btn = tk.Button(add_transaction_container, text="Adicionar Nova Transação", width=36, pady=15, bg="#5f9ea0", fg="white", font=("Calibri", 12, "bold"), command=interface_transaction)
    add_transaction_btn.pack()

    to_excel_container = tk.Frame(win, padx=36, pady=5)
    to_excel_container.pack()
    to_excel_btn = tk.Button(
        to_excel_container,
        text="Ver Transações no Excel",
        width=36,
        pady=15,
        bg="#5f9ea0",
        fg="white",
        font=("Calibri", 12, "bold"),
        command=lambda: interface_exported_to_excel(export_transaction)
    )
    to_excel_btn.pack()

    see_quotation_container = tk.Frame(win, padx=36, pady=5)
    see_quotation_container.pack()
    see_quotation_btn = tk.Button(see_quotation_container, text="Ver Cotação Atual", width=36, pady=15, bg="#5f9ea0", fg="white", font=("Calibri", 12, "bold"), command=interface_quotation)
    see_quotation_btn.pack()

    save_data_container = tk.Frame(win, padx=36, pady=20)
    save_data_container.pack()
    save_data_label = tk.Label(save_data_container, text="[ATENÇÃO]\n\nCaso seja seu primeiro acesso, clique no botão SALVAR DADOS\npara que todos os dados sejam salvos no seu dispositivo.", font=("Calibri", 14, "italic"))
    save_data_label.pack()

    add_transaction_container = tk.Frame(win, padx=36, pady=5)
    add_transaction_container.pack()
    add_transaction_btn = tk.Button(add_transaction_container, text="SALVAR DADOS", width=36, pady=15, bg="#5f9ea0", fg="white", font=("Calibri", 12, "bold"), command=create_database)
    add_transaction_btn.pack()
