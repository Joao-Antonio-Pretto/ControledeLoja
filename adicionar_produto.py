import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def adicionar_produto():
    root = tk.Tk()
    root.title("Adicionar Produto")
    root.geometry("450x280")
    root.resizable(False, False)  # Impede o redimensionamento da janela
    
    # Estilos
    style = ttk.Style(root)
    style.configure('TButton', background='lightblue', font=('Arial', 10), padding=10)
    style.configure('TLabel', font=('Arial', 10), padding=2)
    
    #==============================================================Frames=================================================
    # Frame para ações (botões, entradas e saídas)
    frame_principal = ttk.Frame(root)
    frame_principal.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
    frame_principal.grid_columnconfigure(0, weight=0)
    frame_principal.grid_columnconfigure(1, weight=2)

    product_label = ttk.Label(frame_principal, text="Nome do Produto:")
    product_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    product_entry = ttk.Entry(frame_principal)
    product_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew', columnspan=2)

    quantity_label = ttk.Label(frame_principal, text="Quantidade:")
    quantity_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
    quantity_entry = ttk.Entry(frame_principal)
    quantity_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew', columnspan=2)

    price_label = ttk.Label(frame_principal, text="Preço (R$):")
    price_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
    price_entry = ttk.Entry(frame_principal)
    price_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew', columnspan=2)

    fornecedor_label = ttk.Label(frame_principal, text="Fornecedor:")
    fornecedor_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
    fornecedor_entry = ttk.Entry(frame_principal)
    fornecedor_entry.grid(row=3, column=1, padx=5, pady=5, sticky='ew', columnspan=2)

    adicionar_button = ttk.Button(frame_principal, text="Adicionar") #futuramente deve chamar uma função para adicionar o produto ao banco de dados
    adicionar_button.grid(row=4, column=0, padx=5, pady=5, sticky='ew', columnspan=3)

    sair_button = ttk.Button(frame_principal, text="Sair", command=root.destroy)
    sair_button.grid(row=5, column=0, padx=5, pady=5, sticky='ew', columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    adicionar_produto()
