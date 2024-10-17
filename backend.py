# Importando módulos necessários
from bd import *  # Importa funções para manipulação de banco de dados
from tkinter import *  # Importa módulos do Tkinter para GUI
from tkinter.messagebox import *  # Importa funções de mensagem para mostrar erros e informações
from frontend import *  # Importa componentes da interface gráfica do usuário

# Função para popular uma Treeview com dados de um banco de dados
def info_treeview(tree, tabela, coluna, valor):
    # Abre o banco de dados e obtém todos os dados correspondentes
    resultado = abrir_bd_fetchall("*", tabela, coluna, valor)
    colunas = tree["columns"]  # Obtém as colunas da Treeview

    # Insere cada resultado na Treeview
    for i in resultado:
        valores = i[:len(colunas)]  # Obtém os valores a serem inseridos
        tree.insert("", "end", values=valores)  # Insere os valores na Treeview

# Função para remover um item selecionado da Treeview e do banco de dados
def remover_item(tree, tabela, coluna, index_info):
    selected_item = tree.selection()  # Obtém o item selecionado

    # Verifica se um item foi selecionado
    if not selected_item:
        showerror("ERRO", "Selecione um produto para usar esta função")
    else:
        # Pergunta ao usuário se ele realmente deseja remover o item
        yesno = askyesno("Confirmação", "Voce realmente deseja remover este(s) item?")
        if yesno:
            for i in selected_item:
                valor = tree.item(i, "values")[index_info]  # Obtém o valor do item selecionado
                delete_bd(tabela, coluna, valor)  # Remove o item do banco de dados
                tree.delete(i)  # Remove o item da Treeview

# Função para editar um item selecionado na Treeview
def editar_item(self, tree, button, lista_de_entry, inicio):
    self.selected_item = tree.selection()  # Obtém o item selecionado

    # Verifica se um item foi selecionado
    if not self.selected_item:
        showerror("ERRO", "Selecione um produto para usar esta função")
    elif len(self.selected_item) > 1:
        showerror("ERRO", "Não é possivel editar mais de um item de uma vez")
    else:
        button.config(text="Finalizar Edição")  # Altera o texto do botão
        info = []  # Lista para armazenar as informações do item

        colunas = tree["columns"]  # Obtém as colunas da Treeview
        # Coleta as informações do item selecionado
        for i in range(inicio, len(colunas)):
            infos = tree.item(self.selected_item, "values")[i]
            info.append(infos)

        # Preenche as entradas com as informações do item selecionado
        for entry, new_info in zip(lista_de_entry, info):
            entry.delete(0, END)  # Limpa a entrada
            entry.insert(0, new_info)  # Insere o novo valor
            entry.configure(fg="black")  # Altera a cor do texto para preto

# Função para pesquisar itens na Treeview
def pesquisar_item(self, tree, lista_de_tuplas, tabela, columns, banco):
    valor = self.combobox_pesquisa.get()  # Obtém o valor da combobox
    pesquisar_valor = f"{self.entry_pesquisa.get()}%"  # Obtém o valor da entrada de pesquisa com coringa

    # Realiza a pesquisa dependendo do valor selecionado na combobox
    if valor == "Filtro" or valor == "Todos":
        resultado = pesquisar_tudo(tabela, columns, pesquisar_valor)
    for valor_pesquisa, coluna_bd in lista_de_tuplas:
        if valor == valor_pesquisa:
            resultado = like_bd(banco, coluna_bd, pesquisar_valor)

    # Limpa a Treeview antes de inserir novos resultados
    for item in tree.get_children():
        tree.delete(item)

    colunas = tree["columns"]  # Obtém as colunas da Treeview

    # Insere os resultados da pesquisa na Treeview
    for i in resultado:
        valores = i[:len(colunas)]
        tree.insert("", "end", values=valores)

# Função para pesquisar itens usando JOIN no banco de dados
def pesquisar_item_join(self):
    valor = self.combobox_pesquisa.get()  # Obtém o valor da combobox
    pesquisar_valor = f"{self.entry_pesquisa.get()}%"  # Obtém o valor da entrada de pesquisa com coringa

    # Realiza a pesquisa dependendo do valor selecionado na combobox
    if valor == "Alimento":
        resultado = pesquisar_join_bd("dim_refeicao", "dim_alimento", "alimento", "id_alimento", "nome", pesquisar_valor)
    elif valor == "Dieta":
        resultado = pesquisar_join_bd("dim_refeicao", "dim_dieta", "dieta", "id_dieta", "nome", pesquisar_valor)
    elif valor == "Filtro" or valor == "Todos":
        cursor.execute(""" SELECT * FROM dim_refeicao
                                JOIN dim_alimento ON dim_refeicao.alimento = dim_alimento.id_alimento
                                JOIN dim_dieta ON dim_refeicao.dieta = dim_dieta.id_dieta
                                WHERE dim_alimento.nome LIKE %s
                                AND dim_dieta.nome LIKE %s
                                AND dim_refeicao.horario LIKE %s
                                AND dim_refeicao.medida LIKE %s
                                """, 
        (pesquisar_valor, pesquisar_valor, pesquisar_valor, pesquisar_valor))

        resultado = cursor.fetchall()  # Obtém todos os resultados da consulta

    # Limpa a Treeview antes de inserir novos resultados
    for valor_pesquisa, coluna_bd in [("ID", "id_refeicao"),("Horário", "horario"), ("Medida", "medida")]:
        if valor == valor_pesquisa:
            resultado = like_bd("dim_refeicao", coluna_bd, pesquisar_valor)

    for item in self.tree_refeicao.get_children():
        self.tree_refeicao.delete(item)  # Limpa a Treeview

    # Insere os resultados da pesquisa na Treeview
    for i in resultado:
        alimento = valores_fatos("dim_alimento", "nome", "id_alimento", i[1])
        dieta = valores_fatos("dim_dieta", "nome", "id_dieta", i[2])
        self.tree_refeicao.insert("", "end", values=(i[0], alimento, dieta, i[3], i[4]))

# Função para cadastrar uma dieta
def cadastrar_dieta(self):
    resultado = abrir_bd_fetchone("dim_usuario", "cpf", self.entry_cpfpaciente.get())  # Verifica se o CPF existe no banco

    # Verifica se todos os campos estão preenchidos
    if any(entry in ["Nome:", "CPF Paciente:", "Refeições:", "Calorias Diárias"] or entry.strip() == "" for entry in [self.entry_nome.get(), self.entry_cpfpaciente.get(), self.entry_refeicoes.get(), self.entry_caloriasdiarias.get()]):
        showerror("ERRO", "Preencha todos os campos para fazer cadastro")
        return

    # Valida o CPF do paciente
    elif not self.entry_cpfpaciente.get().isnumeric():
        showerror("ERRO",  "Insira apenas números no campo 'CPF Paciente'")
        return    
    elif not self.entry_refeicoes.get().isnumeric():
        showerror("ERRO",  "Insira apenas números no campo 'Refeições'")
        return
    elif len(self.entry_cpfpaciente.get()) > 11 or len(self.entry_cpfpaciente.get()) < 11:
        showerror("ERRO", "O campo 'CPF Paciente' está incorreto")
        return
    elif not resultado:
        showerror("ERRO", "Não existe ninguem cadastrado com este cpf")
        return
    if resultado[8] == 1:
        showerror("ERRO", "Não existe paciente cadastrado com este CPF")
        return

    # Valida a entrada de calorias diárias
    try:
        calorias = float(self.entry_caloriasdiarias.get())
        if calorias <= 0:
            showerror("ERRO", "O valor de 'Calorias Diárias' deve ser maior que zero")
            return
    except ValueError:
        showerror("ERRO", "Insira apenas números no campo 'Calorias Diárias'")
        return

    # Realiza o cadastro ou edição de uma dieta
    if self.button_cadastrar.cget("text") == "Cadastrar":              
        resultado = abrir_bd_fetchone("dim_dieta", "cpf_paciente", self.entry_cpfpaciente.get())
          
        if resultado:
            showerror("ERRO", "Já existe uma dieta com este cpf")
        else:    
            inserir_bd("dim_dieta", ["nome", "cpf_paciente", "refeicoes", "calorias_diarias"], (self.entry_nome.get(), self.entry_cpfpaciente.get(), self.entry_refeicoes.get(), self.entry_caloriasdiarias.get()))
            showinfo("SUCESSO", "Cadastro concluido!")  # Most
