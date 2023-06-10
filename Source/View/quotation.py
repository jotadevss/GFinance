import tkinter as tk
from Source.Controller.controller import *
from Source.View.Components.backButton import *


def interface_quotation():
    # Interface for displaying real-time quotes
    quotations = get_quotation()
    dolar = quotations["USD"]
    euro = quotations["EUR"]
    bitcoin = quotations["BTC"]

    qtUI = tk.Toplevel()
    qtUI.title("Cotações em Tempo Real")
    qtUI.geometry("800x800")
    qtUI.config(padx=10, pady=100)
    qtUI.resizable(width=False, height=False)

    header_label = tk.Label(qtUI, text="Veja todas as cotações do dia de hoje em tempo real!", font=("Calibri", 18, "italic"))
    header_label.pack(pady=10)

    title_dolar_label = tk.Label(qtUI, text="Dólar Americano", bg="#5f9ea0", fg="white", font=("Calibri", 16, "bold"))
    title_dolar_label.pack(pady=10)
    value_dolar_label = tk.Label(qtUI, text=f"$1 USD   ->   R$ {dolar:.2f} BRL", font=("Calibri", 14))
    value_dolar_label.pack(pady=0)

    title_euro_label = tk.Label(qtUI, text="Euro", bg="#5f9ea0", fg="white", font=("Calibri", 16, "bold"))
    title_euro_label.pack(pady=10)
    value_euro_label = tk.Label(qtUI, text=f"€1 EUR   ->   R$ {euro:.2f} BRL", font=("Calibri", 14))
    value_euro_label.pack(pady=0)

    title_btc_label = tk.Label(qtUI, text="Bitcoin", bg="#5f9ea0", fg="white", font=("Calibri", 16, "bold"))
    title_btc_label.pack(pady=10)
    value_btc_label = tk.Label(qtUI, text=f"₿1 BTC   ->   R$ {bitcoin:.2f} BRL", font=("Calibri", 14))
    value_btc_label.pack(pady=0)

    back_button(qtUI, qtUI.destroy)
