import tkinter as tk
from tkinter import messagebox

#Definição do que cada botão faz
def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    print(f"Usuário: {usuario}, Senha: {senha}")
    if usuario == "admin" and senha == "1234":
        root.destroy()
        from main import janela_estoque
        janela_estoque()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")
        entry_usuario.delete(0, tk.END)
        entry_senha.delete(0, tk.END)

def limpar():
    entry_usuario.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    print("Campos limpos")

def sair():
    root.destroy()
    print("Aplicação fechada")

root = tk.Tk()
root.title("Login")
root.geometry("250x250")
root.resizable(False, False)  # Impede o redimensionamento da janela
root.configure(bg="lightblue")

# Frame principal que contém tudo
main_frame = tk.Frame(root, bg="lightblue")
main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20) # Frame ocupando toda a tela, espaçamento de 20 pixels em cada lado

# Frame para os campos de entrada
entry_frame = tk.Frame(main_frame, bg="lightblue")
entry_frame.pack(expand=True)

# Configurar pesos para centralização (feito pela IA, possivelmente inútil e com possibilidade de fazer de outra forma)
entry_frame.grid_rowconfigure(0, weight=1)
entry_frame.grid_rowconfigure(6, weight=1)  # Linhas extras para ajudar na centralização
entry_frame.grid_columnconfigure(0, weight=1)
entry_frame.grid_columnconfigure(2, weight=1)

# Rótulos e entradas
label_usuario = tk.Label(entry_frame, text="Usuário:", bg="lightblue")
label_usuario.grid(row=1, column=0, padx=5, pady=5, sticky="e") #alinhado ao leste

entry_usuario = tk.Entry(entry_frame)
entry_usuario.grid(row=1, column=1, padx=5, pady=5)

label_senha = tk.Label(entry_frame, text="Senha:", bg="lightblue")
label_senha.grid(row=2, column=0, padx=5, pady=5, sticky="e")

entry_senha = tk.Entry(entry_frame, show="*") #mostra asterisco em vez de texto
entry_senha.grid(row=2, column=1, padx=5, pady=5)

# Botões centralizados
botao_login = tk.Button(entry_frame, text="Login", command=login)
botao_login.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")

botao_limpar = tk.Button(entry_frame, text="Limpar", command=limpar)
botao_limpar.grid(row=4, column=0, columnspan=2, pady=5, sticky="nsew")

botao_sair = tk.Button(entry_frame, text="Sair", command=sair)
botao_sair.grid(row=5, column=0, columnspan=2, pady=5, sticky="nsew")

root.mainloop()