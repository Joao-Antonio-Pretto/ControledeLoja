import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def janela_estoque():
    root = tk.Tk()
    root.title("Estoque")
    root.geometry("700x900")

    # Frames
    # Frame para ações (botões)
    frame_acoes = ttk.Frame(root)
    frame_acoes.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
    ttk.Label(frame_acoes, text="Ações:").pack(side=tk.LEFT, padx=5) #apenas para posicionar




    ################################Criação da tabela###############################
    # Frame para a tabela
    frame_tabela = ttk.Frame(root)
    frame_tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Definição das colunas
    colunas = ("id", "produto", "quantidade", "preco")
    tree = ttk.Treeview(frame_tabela, columns=colunas, show='headings') # show='headings' para não mostrar a coluna vazia inicial (padrão). columns=colunas define onde está o identificador de cada coluna

    # Declaração das colunas, baseado nas variáveis de identificadores acima
    tree.heading("id", text="ID") #.heading associa o identificador da coluna com o texto que será exibido
    tree.heading("produto", text="Nome")
    tree.heading("quantidade", text="Quantidade")
    tree.heading("preco", text="Preço (R$)")
    # Largura das colunas
    tree.column("id", width=50)# .column associa o identificador da coluna com a largura que será exibida
    tree.column("produto", width=250)
    tree.column("quantidade", width=100)
    tree.column("preco", width=100)

    tree.pack(fill=tk.BOTH, expand=True)# aqui adiciona a tabela na janela

    # Adicionando dados de exemplo
    dados_exemplo = [
        (1, 'Mouse Gamer RGB', 50, '85.00'),
        (2, 'Teclado Mecânico', 35, '250.50'),
        (3, 'Monitor 24" 144Hz', 20, '1400.00'),
        (4, 'Headset 7.1', 40, '350.75'),
        (5, 'SSD 1TB NVMe', 30, '600.00')
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