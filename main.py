import tkinter as tk
from tkinter import messagebox
import pickle


janela = tk.Tk()  # Cria a janela principal da aplicação
janela.title('Lista de Tarefas')  # Define o título da janela



tarefas = []  # Inicializa uma lista vazia para armazenar as tarefas

# Função para adicionar tarefas
def adicionar_tarefa():
    tarefa = entrada.get()  # Obtém o texto da tarefa a partir da entrada de texto
    if tarefa != "":  # Verifica se a tarefa não está vazia
        tarefas.append(tarefa)  # Adiciona a tarefa à lista
        atualizar_lista()  # Atualiza a lista exibida
        entrada.delete(0, tk.END)  # Limpa o campo de entrada
    else:
        messagebox.showwarning("Aviso", "A tarefa não pode ser vazia!")  # Exibe um aviso se a tarefa estiver vazia

# Função para remover tarefas
def remover_tarefa():
    try:
        indice = listbox.curselection()[0]  # Obtém o índice da tarefa selecionada
        tarefas.pop(indice)  # Remove a tarefa da lista usando o índice
        atualizar_lista()  # Atualiza a lista exibida
    except IndexError:
        messagebox.showwarning("Aviso!", "Selecione uma tarefa para remover.")  # Exibe um aviso se nenhuma tarefa estiver selecionada

# Função para listar (carregar) tarefas do arquivo
def listar_tarefas():
    global tarefas  # Usa a variável global 'tarefas'
    try:
        with open("tarefas.pickle", "rb") as f:  # Abre o arquivo em modo de leitura binária
            tarefas = pickle.load(f)  # Carrega as tarefas do arquivo
        atualizar_lista()  # Atualiza a lista exibida
    except FileNotFoundError:
        tarefas = []  # Inicializa a lista de tarefas como vazia

# Função para atualizar a lista de tarefas na interface
def atualizar_lista():
    listbox.delete(0, tk.END)  # Limpa todos os itens da Listbox
    for tarefa in tarefas:  # Itera sobre todas as tarefas
        listbox.insert(tk.END, tarefa)  # Insere cada tarefa na Listbox


# Função para marcar uma tarefa como concluída
def marcar_como_concluida():
    try:
        indice = listbox.curselection()[0]  # Obtém o índice da tarefa selecionada
        tarefa = tarefas[indice]  # Obtém a tarefa a partir do índice
        tarefas[indice] = f"{tarefa} (Concluída)"  # Marca a tarefa como concluída
        atualizar_lista()  # Atualiza a lista exibida
    except IndexError:
        messagebox.showwarning("Aviso!", "Selecione uma tarefa para marcar como concluída.")  # Exibe um aviso se nenhuma tarefa estiver selecionada

# Criando interface gráfica
frame = tk.Frame(janela) #Cria a janela
frame.pack(pady=10) #Deixa a janela com o menor tamanho

entrada = tk.Entry(frame, width=30) #Campo de entradada de texto para a tarefa
entrada.pack(side=tk.LEFT, padx=10) #Posição e tamanho do campo de entrada de tarefas

botao_adicionar = tk.Button(frame, text="Adicionar Tarefa", command= adicionar_tarefa, bg = '#87CEEB') #Configura o botão de adicionar tarefas
botao_adicionar.pack(side=tk.LEFT) #Adiona o botão na posição

listbox = tk.Listbox(janela, width=20, height=20) #Configura a área da lista de tarefas
listbox.pack(pady=10) # Adiciona a área

botao_remover = tk.Button(text="Remover Tarefa",command= remover_tarefa, bg='#CD5C5C') #Configura o botão para remover tarefas
botao_remover.pack(side= tk.BOTTOM) #Adicionando o botão na parte de baixo

botao_concluido = tk.Button(text="Concluir Tarefa", command= marcar_como_concluida, bg='#00FF7F')
botao_concluido.pack(side= tk.BOTTOM) 



janela.mainloop()