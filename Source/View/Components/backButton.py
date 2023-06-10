import tkinter as tk

def back_button(frame, close_func):
    # Function to create a back button
    back_btn = tk.Button(frame, text="Voltar para o Início", width=20, pady=15, command=close_func, bg="#5f9ea0", fg="white", font=("Calibri", 12, "bold"))
    back_btn.pack(pady=30)