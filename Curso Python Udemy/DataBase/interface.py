import tkinter as tk
from tkinter import messagebox
import dados1

def adicionar_filme():
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    dados1.inserir_dados(nome, ano, nota)
    messagebox.showinfo("Filme cadastrado com sucesso.")

def atualizar_filme():
    id = entry_id.get()
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    dados1.atualizar_dados(id, nome, ano, nota)
    messagebox.showinfo("Filme atualizado com sucesso.")

def excluir_filme():
    id = entry_id.get()
    dados1.excluir_dados(id)
    messagebox.showinfo("Filme excluído com sucesso.")

# Interface Gráfica
root = tk.Tk()
root.title("Gerenciador de Filmes")

# Rótulos e campos de entrada
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome = tk.Label(root, text="ID:")
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_ano = tk.Label(root, text="ID:")
label_ano.grid(row=2, column=0)
entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, padx=10, pady=5)

label_nota = tk.Label(root, text="ID:")
label_nota.grid(row=3, column=0)
entry_nota = tk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, padx=10, pady=5)

button_adicionar = tk.Button(root, text="Adicionar Filme", command=adicionar_filme)
button_adicionar.grid(row=4, column=0, columnspan=2, pady=5)

button_atualizar = tk.Button(root, text="Adicionar Filme", command=atualizar_filme)
button_atualizar.grid(row=5, column=0, columnspan=2, pady=5)

button_excluir = tk.Button(root, text="Adicionar Filme", command=excluir_filme)
button_excluir.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()