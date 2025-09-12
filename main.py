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
    root.maxsize(800, 1000)  # Define o tamanho máximo da janela

    #==============================================================Frames=================================================
    # Frame para a barra de menu

    # Estilos
    style = ttk.Style(root)
    style.theme_use('clam')  # Tema 'clam' é mais moderno e limpo de acordo com a documentação do ttk
    style.configure('Principal.TButton', background='white', font=('Arial', 12), padding=20) #configuração dos botões grandes
    style.configure("Small.TButton", background='lightcoral', foreground='blue', font=('Arial', 10), padding=5) #configuração do botão de sair
    style.configure('TLabel', font=('Arial', 12), padding=2) #configuração dos rótulos
    style.configure('TEntry', font=('Arial', 12), padding=2) #configuração das entradas de texto
    style.configure('Treeview', font=('Arial', 12), rowheight=23) #configuração das linhas da tabela
    style.configure('Vertical.TScrollbar', background='white', arrowsize=10)  #configuração da scrollbar da tabela

    # Frame para ações (botões, entradas e saídas)
    frame_acoes = ttk.Frame(root)
    frame_acoes.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    frame_acoes.grid_columnconfigure(0, weight=1)
    frame_acoes.grid_columnconfigure(1, weight=3)
    frame_acoes.grid_columnconfigure(2, weight=1)

    label_produto = ttk.Label(frame_acoes, text="ID do Produto:")
    label_produto.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
    entry_produto = ttk.Entry(frame_acoes)
    entry_produto.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

    label_descricao = ttk.Label(frame_acoes, text="Nome do Produto:")
    label_descricao.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
    entry_descricao = ttk.Entry(frame_acoes)
    entry_descricao.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

    label_quantidade = ttk.Label(frame_acoes, text="Quantidade:")
    label_quantidade.grid(row=2, column=0, padx=5, pady=5, sticky='ew')
    entry_quantidade = ttk.Entry(frame_acoes)
    entry_quantidade.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

    label_preco = ttk.Label(frame_acoes, text="Preço (R$):")
    label_preco.grid(row=3, column=0, padx=5, pady=5, sticky='ew')
    entry_preco = ttk.Entry(frame_acoes)
    entry_preco.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

    label_fornecedor = ttk.Label(frame_acoes, text="Fornecedor:")
    label_fornecedor.grid(row=4, column=0, padx=5, pady=5, sticky='ew')
    entry_fornecedor = ttk.Entry(frame_acoes)
    entry_fornecedor.grid(row=4, column=1, padx=5, pady=5, sticky='ew')

    # Botões
    add_button = ttk.Button(frame_acoes, text="Adicionar", command=adicionar_produto, style='Principal.TButton')
    add_button.grid(row=0, column=2, rowspan=2, padx=8, pady=10, sticky='nsew')

    remove_button = ttk.Button(frame_acoes, text="Remover", style='Principal.TButton') #futuramente deve chamar uma função para remover o produto do banco de dados
    remove_button.grid(row=3, column=2, rowspan=2, padx=8, pady=10, sticky='nsew')

    ################################Criação da tabela###############################

    # Frame para a tabela
    frame_tabela = ttk.Frame(root)
    frame_tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Definição das colunas
    colunas = ("id", "produto", "quantidade", "preco", "fornecedor") # Identificadores das colunas
    tree = ttk.Treeview(frame_tabela, columns=colunas, show='headings') # show='headings' para não mostrar a coluna vazia inicial (padrão). columns=colunas define onde está o identificador de cada coluna

    # Barra de rolagem
    scrollbar = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=tree.yview) # cria a barra de rolagem na vertical e dá o comando de controlar o eixo y
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # posiciona a barra de rolagem na direita e faz ela preencher o eixo y
    tree.configure(yscrollcommand=scrollbar.set) # a tabela diz o tamanho da barra de rolagem

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
        (5, 'SSD 1TB NVMe', 30, '600.00', 'Fornecedor E'),
        (6, 'Placa de Vídeo RTX 3060', 15, '2200.00', 'Fornecedor F'),
        (7, 'Fonte 650W 80 Plus', 25, '450.00', 'Fornecedor G'),
        (8, 'Gabinete Mid Tower', 10, '300.00', 'Fornecedor H'),
        (9, 'Cooler para CPU', 45, '120.00', 'Fornecedor I'),
        (10, 'Cadeira Gamer', 5, '900.00', 'Fornecedor J'),
        (11, 'Webcam 1080p', 20, '250.00', 'Fornecedor K'),
        (12, 'Roteador Wi-Fi 6', 18, '400.00', 'Fornecedor L'),
        (13, 'Memória RAM 16GB', 60, '320.00', 'Fornecedor M'),
        (14, 'Placa-Mãe ATX', 12, '800.00', 'Fornecedor N'),
        (15, 'Processador Intel i7', 8, '1500.00', 'Fornecedor O'),
        (16, 'Cabo HDMI 2.0', 100, '50.00', 'Fornecedor P'),
        (17, 'Adaptador USB-C', 70, '80.00', 'Fornecedor Q'),
        (18, 'Impressora Multifuncional', 6, '1200.00', 'Fornecedor R'),
        (19, 'Scanner de Documentos', 9, '700.00', 'Fornecedor S'),
        (20, 'Projetor Portátil', 4, '2500.00', 'Fornecedor T'),
        (21, 'Estabilizador de Energia', 14, '350.00', 'Fornecedor U'),
        (22, 'Hub USB 3.0', 55, '150.00', 'Fornecedor V'),
        (23, 'Leitor de Cartão SD', 80, '90.00', 'Fornecedor W'),
        (24, 'Microfone Condensador', 22, '400.00', 'Fornecedor X'),
        (25, 'Placa de Captura 4K', 7, '1800.00', 'Fornecedor Y'),
        (26, 'Cabo de Rede CAT6', 150, '30.00', 'Fornecedor Z'),
        (27, 'Filtro de Linha', 33, '200.00', 'Fornecedor AA'),
        (28, 'Suporte para Monitor', 11, '250.00', 'Fornecedor AB'),
        (29, 'Mesa para Escritório', 3, '800.00', 'Fornecedor AC'),
        (30, 'Luminária LED para Mesa', 27, '120.00', 'Fornecedor AD'),
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