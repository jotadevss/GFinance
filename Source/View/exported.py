import tkinter as tk
from Source.View.Components.backButton import *


def interface_exported_to_excel(export_to_excel):
    # Interface for displaying completion of export to Excel
    export_to_excel()

    exUI = tk.Toplevel()
    exUI.title("Exportação Concluída")
    exUI.geometry("800x600")
    exUI.config(padx=10, pady=100)
    exUI.resizable(width=False, height=False)

    header_label = tk.Label(exUI, text="Exportação do Arquivo Excel Concluída", font=("Calibri", 18, "italic"))
    header_label.pack(pady=10)

    back_button(exUI, exUI.destroy)
