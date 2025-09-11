import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from adicionar_produto import adicionar_produto

def janela_estoque():
    root = tk.Tk() # Criação da janela principal
    root.title("Estoque")
    root.geometry("600x800")
    min_width = 600 # Define a largura mínima da janela
    min_height = 800 # Define a altura mínima da janela
    root.minsize(min_width, min_height)  # Define o tamanho mínimo da janela

    #==============================================================Frames=================================================
    # Frame para a barra de menu

    # Estilos
    style = ttk.Style(root)
    style.theme_use('clam')  # Tema 'clam' é mais moderno e limpo de acordo com a documentação do ttk
    style.configure('TButton', font=('Arial', 12), padding=20)
    style.configure("Small.TButton", background='lightcoral', foreground='blue', font=('Arial', 10), padding=5)
    style.configure('TLabel', font=('Arial', 12), padding=2)
    style.configure('TEntry', font=('Arial', 12), padding=2)
    style.configure('Treeview', font=('Arial', 12), rowheight=25)

    # Frame para ações (botões, entradas e saídas)
    frame_acoes = ttk.Frame(root)
    frame_acoes.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    frame_acoes.grid_columnconfigure(0, weight=1)
    frame_acoes.grid_columnconfigure(1, weight=3)
    frame_acoes.grid_columnconfigure(2, weight=1)

    label_produto = ttk.Label(frame_acoes, text="ID do Produto:")
    label_produto.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
    entry_produto = ttk.Entry(frame_acoes)
    entry_produto.grid(row=0, column=1, padx=5, pady=5, sticky='w')

    label_descricao = ttk.Label(frame_acoes, text="Nome do Produto:")
    label_descricao.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
    entry_descricao = ttk.Entry(frame_acoes)
    entry_descricao.grid(row=1, column=1, padx=5, pady=5, sticky='w')

    label_quantidade = ttk.Label(frame_acoes, text="Quantidade:")
    label_quantidade.grid(row=2, column=0, padx=5, pady=5, sticky='ew')
    entry_quantidade = ttk.Entry(frame_acoes)
    entry_quantidade.grid(row=2, column=1, padx=5, pady=5, sticky='w')

    label_preco = ttk.Label(frame_acoes, text="Preço (R$):")
    label_preco.grid(row=3, column=0, padx=5, pady=5, sticky='ew')
    entry_preco = ttk.Entry(frame_acoes)
    entry_preco.grid(row=3, column=1, padx=5, pady=5, sticky='w')

    label_fornecedor = ttk.Label(frame_acoes, text="Fornecedor:")
    label_fornecedor.grid(row=4, column=0, padx=5, pady=5, sticky='ew')
    entry_fornecedor = ttk.Entry(frame_acoes)
    entry_fornecedor.grid(row=4, column=1, padx=5, pady=5, sticky='w')

    # Botões
    add_button = ttk.Button(frame_acoes, text="Adicionar", command=adicionar_produto)
    add_button.grid(row=0, column=2, rowspan=2, padx=8, pady=10, sticky='nsew')

    remove_button = ttk.Button(frame_acoes, text="Remover")
    remove_button.grid(row=3, column=2, rowspan=2, padx=8, pady=10, sticky='nsew')

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
    tree.column("id", width=30)# .column associa o identificador da coluna com a largura que será exibida
    tree.column("produto", width=250)
    tree.column("quantidade", width=80)
    tree.column("preco", width=80)
    tree.column("fornecedor", width=130)

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
    frame_status.grid_columnconfigure(0, weight=1)
    sair_button = ttk.Button(frame_status, text="Sair", style="Small.TButton", command=root.destroy)
    sair_button.grid(row=0, column=0, padx=5, pady=5, sticky='e')

    root.mainloop()



if __name__ == "__main__":
    janela_estoque()