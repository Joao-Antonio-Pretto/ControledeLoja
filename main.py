import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def janela_estoque():
    root = tk.Tk() # Criação da janela principal
    root.title("Estoque")
    root.geometry("700x900")

    #==============================================================Frames=================================================
    # Frame para a barra de menu



    # Frame para ações (botões, entradas e saídas)
    frame_acoes = ttk.Frame(root)
    frame_acoes.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    label_produto = ttk.Label(frame_acoes, text="ID do Produto:")
    label_produto.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    entry_produto = ttk.Entry(frame_acoes)
    entry_produto.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

    label_descricao = ttk.Label(frame_acoes, text="Nome do Produto:")
    label_descricao.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    entry_descricao = ttk.Entry(frame_acoes)
    entry_descricao.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

    label_quantidade = ttk.Label(frame_acoes, text="Quantidade:")
    label_quantidade.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    entry_quantidade = ttk.Entry(frame_acoes)
    entry_quantidade.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

    label_preco = ttk.Label(frame_acoes, text="Preço (R$):")
    label_preco.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    entry_preco = ttk.Entry(frame_acoes)
    entry_preco.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

    label_fornecedor = ttk.Label(frame_acoes, text="Fornecedor:")
    label_fornecedor.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    entry_fornecedor = ttk.Entry(frame_acoes)
    entry_fornecedor.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

    ################################Criação da tabela###############################

    # Frame para a tabela
    frame_tabela = ttk.Frame(root)
    frame_tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Definição das colunas
    colunas = ("id", "produto", "quantidade", "preco", "fornecedor") # Identificadores das colunas
    tree = ttk.Treeview(frame_tabela, columns=colunas, show='headings') # show='headings' para não mostrar a coluna vazia inicial (padrão). columns=colunas define onde está o identificador de cada coluna

    # Declaração das colunas, baseado nas variáveis de identificadores acima
    tree.heading("id", text="ID") #.heading associa o identificador da coluna com o texto que será exibido
    tree.heading("produto", text="Nome")
    tree.heading("quantidade", text="Quantidade")
    tree.heading("preco", text="Preço (R$)")
    tree.heading("fornecedor", text="Fornecedor")
    # Largura das colunas
    tree.column("id", width=50)# .column associa o identificador da coluna com a largura que será exibida
    tree.column("produto", width=250)
    tree.column("quantidade", width=100)
    tree.column("preco", width=100)
    tree.column("fornecedor", width=150)

    tree.pack(fill=tk.BOTH, expand=True)# aqui adiciona a tabela na janela

    # Adicionando dados de exemplo
    dados_exemplo = [
        (1, 'Mouse Gamer RGB', 50, '85.00', 'Fornecedor A'),
        (2, 'Teclado Mecânico', 35, '250.50', 'Fornecedor B'),
        (3, 'Monitor 24" 144Hz', 20, '1400.00', 'Fornecedor C'),
        (4, 'Headset 7.1', 40, '350.75', 'Fornecedor D'),
        (5, 'SSD 1TB NVMe', 30, '600.00', 'Fornecedor E')
    ]

    # Inserindo os dados na tabela
    for item in dados_exemplo:
        tree.insert('', tk.END, values=item)





    # Frame para status ou outras informações
    frame_status = ttk.Frame(root)
    frame_status.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
    ttk.Label(frame_status, text="Status: Pronto").pack(side=tk.LEFT, padx=5) #apenas para posicionar

    root.mainloop()



if __name__ == "__main__":
    janela_estoque()