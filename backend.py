from bd import *
from  tkinter import *
from tkinter.messagebox import *
from frontend import *

##NUTRICIONISTA
def info_treeview(tree, tabela, coluna, valor):
    resultado = abrir_bd_fetchall("*", tabela, coluna, valor)
    colunas = tree["columns"]

    for i in resultado:
    
        valores = i[:len(colunas)]
        tree.insert("", "end", values=valores)

def remover_item(tree, tabela, coluna, index_info):
    selected_item = tree.selection()
    
    if not selected_item:
        showerror("ERRO", "Selecione um produto para usar esta função")
    
    else:
        yesno = askyesno("Confirmação", "Voce realmente deseja remover este(s) item?")
    
        if yesno:
            for i in selected_item:
                valor = tree.item(i, "values")[index_info]
                
                delete_bd(tabela, coluna, valor) 
                tree.delete(i)

def editar_item(self, tree, button, lista_de_entry, inicio):
    self.selected_item = tree.selection()

    if not self.selected_item:
        showerror("ERRO", "Selecione um produto para usar esta função")
    
    elif len(self.selected_item) > 1:
        showerror("ERRO", "Não é possivel editar mais de um item de uma vez")
    
    else:
        button.config(text="Finalizar Edição")
        info = []

        colunas = tree["columns"]
        for i in range(inicio, len(colunas)):
            infos = tree.item(self.selected_item, "values")[i]
            info.append(infos)
        
        for entry, new_info in zip(lista_de_entry, info):
                        
            entry.delete(0, END)
            entry.insert(0, new_info)
            entry.configure(fg="black")

def pesquisar_item(self, tree, lista_de_tuplas, tabela, columns, banco):
    valor = self.combobox_pesquisa.get()
    pesquisar_valor = f"{self.entry_pesquisa.get()}%"

    if valor == "Filtro" or valor == "Todos":
        resultado = pesquisar_tudo(tabela, columns, pesquisar_valor)
    for valor_pesquisa, coluna_bd in lista_de_tuplas:
        if valor == valor_pesquisa:
            resultado = like_bd(banco, coluna_bd, pesquisar_valor)
    
    for item in tree.get_children():
        tree.delete(item)
    
    colunas = tree["columns"]

    for i in resultado:
    
        valores = i[:len(colunas)]
        tree.insert("", "end", values=valores)

def pesquisar_item_join(self):
    valor = self.combobox_pesquisa.get()
    pesquisar_valor = f"{self.entry_pesquisa.get()}%"

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

        resultado = cursor.fetchall()
    
    for valor_pesquisa, coluna_bd in [("ID", "id_refeicao"),("Horário", "horario"), ("Medida", "medida")]:
        if valor == valor_pesquisa:
            resultado = like_bd("dim_refeicao", coluna_bd, pesquisar_valor)
    
    for item in self.tree_refeicao.get_children():
        self.tree_refeicao.delete(item)
    
    for i in resultado:
        alimento = valores_fatos("dim_alimento", "nome", "id_alimento", i[1])
        dieta = valores_fatos("dim_dieta", "nome", "id_dieta", i[2])
        self.tree_refeicao.insert("", "end", values=(i[0], alimento, dieta, i[3], i[4]))

def cadastrar_dieta(self):
    resultado = abrir_bd_fetchone("dim_dieta", "cpf_paciente", self.entry_cpfpaciente.get())
        
    if any(entry == "Nome:" or entry == "CPF Paciente:" or entry == "Refeições:" or entry == "Calorias Diárias" or entry == "" for entry in [self.entry_nome.get(), self.entry_cpfpaciente.get(), self.entry_refeicoes.get(), self.entry_caloriasdiarias.get()]): 
        showerror("ERRO", "Preencha todos os campos para fazer cadastro")
        return
            
    elif not self.entry_cpfpaciente.get().isnumeric():
        showerror("ERRO",  "Insira apenas números no campo 'CPF Paciente'")
        return
        
    elif not self.entry_refeicoes.get().isnumeric():
        showerror("ERRO",  "Insira apenas números no campo 'Refeições'")
        return

    elif len(self.entry_cpfpaciente.get()) > 11 or len(self.entry_cpfpaciente.get()) < 11:
        showerror("ERRO", "O campo 'CPF Paciente' está incorreto")
        return

    try:
        calorias = float(self.entry_caloriasdiarias.get())
        if calorias <= 0:
            showerror("ERRO", "O valor de 'Calorias Diárias' deve ser maior que zero")
            return
    except ValueError:
        showerror("ERRO", "Insira apenas números no campo 'Calorias Diárias'")
        return

    if self.button_cadastrar.cget("text") == "Cadastrar":                
        if resultado:
            showerror("ERRO", "Já existe uma dieta com este cpf")

        else:    
            inserir_bd("dim_dieta", ["nome", "cpf_paciente", "refeicoes", "calorias_diarias"], (self.entry_nome.get(), self.entry_cpfpaciente.get(), self.entry_refeicoes.get(), self.entry_caloriasdiarias.get()))

    elif self.button_cadastrar.cget("text") == "Finalizar Edição":
        id_dieta = self.tree_dietas.item(self.selected_item, "values")[0]
    
        for coluna, valor in [("nome", self.entry_nome.get()), 
                                ("cpf_paciente", self.entry_cpfpaciente.get()), 
                                ("refeicoes", self.entry_refeicoes.get()), 
                                ("calorias_diarias", self.entry_caloriasdiarias.get())]:
                
            atualizar_bd(coluna, valor, "dieta", id_dieta)
        conexao.commit()
        
    else:
        showerror("ERRO", "Reinicie o aplicativo")

    for item in self.tree_dietas.get_children():
        self.tree_dietas.delete(item)
    
    info_treeview(self.tree_dietas, "dim_dieta", None, None)

    self.button_cadastrar.config(text="Cadastrar")
        

def cadastrar_alimento(self):
    resultado = abrir_bd_fetchone("dim_alimento", "nome", self.entry_nome.get())

    if any(entry == "Nome:" or entry == "Calorias:" or entry == "Proteínas:" or entry == "Carboidratos:" or entry == "Gorduras:" or entry == "" for entry in [self.entry_nome.get(), self.entry_caloria.get(), self.entry_proteina.get(), self.entry_carboidrato.get(), self.entry_gordura.get()]): 
            showerror("ERRO", "Preencha todos os campos para fazer cadastro")
            return


    for i in [self.entry_caloria.get(), self.entry_carboidrato.get(), self.entry_gordura.get(), self.entry_proteina.get()]:
        try:
            float(i)
            if float(i) <=0:
                showerror("ERRO", "Insira apenas valores acima de 0 nos campos de valores")
                return
        
        except ValueError:
            showerror("ERRO", "Insira apenas valores numericos nos campos de valores")
            return

    if self.button_cadastrar.cget("text") == "Cadastrar":
        
        if resultado:
            showerror("ERRO", "Este alimento ja existe no sistema")
            return
        
        inserir_bd("dim_alimento", ["nome", "caloria", "proteina", "carboidrato", "gordura"], (self.entry_nome.get(), self.entry_caloria.get(), self.entry_proteina.get(), self.entry_carboidrato.get(), self.entry_gordura.get()))
    
    elif self.button_cadastrar.cget("text") == "Finalizar Edição":
        id_alimento = self.tree_alimentos.item(self.selected_item, "values")[0]
            
        for coluna, valor in [("nome", self.entry_nome.get()), 
                                ("caloria", self.entry_caloria.get()), 
                                ("proteina", self.entry_proteina.get()), 
                                ("carboidrato", self.entry_carboidrato.get()),
                                ("gordura", self.entry_gordura.get())]:
                
            atualizar_bd(coluna, valor, "alimento", id_alimento)
        conexao.commit()
    
    for item in self.tree_alimentos.get_children():
        self.tree_alimentos.delete(item)

    info_treeview(self.tree_alimentos, "dim_alimento", None, None)

    self.button_cadastrar.config(text="Cadastrar")

def cadastrar_refeicao(self):
    id_alimento = valores_fatos("dim_alimento", "id_alimento", "nome", self.combobox_alimento.get())
    id_dieta = valores_fatos("dim_dieta", "id_dieta", "nome", self.combobox_dieta.get())

    if id_alimento == "None" or id_dieta == "None":
        showerror("ERRO", "Dieta ou Alimento nao existentes")
        return
    
    if self.button_cadastrar.cget("text") == "Cadastrar":
        inserir_bd("dim_refeicao", ["alimento", "dieta", "horario", "medida"], (id_alimento, id_dieta, self.entry_horario.get(), self.entry_medida.get()))
    
    elif self.button_cadastrar.cget("text") == "Finalizar Edição":
        id_refeicao = self.tree_refeicao.item(self.selected_item, "values")[0]

        for coluna, valor in [("alimento", id_alimento),
                                ("dieta", id_dieta),
                                ("horario", self.entry_horario.get()),
                                ("medida", self.entry_medida.get())]:
            atualizar_bd(coluna, valor, "refeicao", id_refeicao)
        conexao.commit()

    for item in self.tree_refeicao.get_children():
        self.tree_refeicao.delete(item)
    
    info_treeview_refeicao(self)

    self.button_cadastrar.config(text="Cadastrar")

def info_treeview_refeicao(self):
    resultado = abrir_bd_fetchall("*", "dim_refeicao", None, None)

    for i in resultado:
        id_alimento = valores_fatos("dim_alimento", "nome", "id_alimento", i[1])
        id_dieta = valores_fatos("dim_dieta", "nome", "id_dieta", i[2])

        self.tree_refeicao.insert("", "end", values=(i[0], id_alimento, id_dieta, i[3], i[4]))

def editar_combobox_refeicao(self):
    self.selected_item = self.tree_refeicao.selection()

    if not self.selected_item:
        showerror("ERRO", "Selecione um produto para usar esta função")
        return
    if len(self.selected_item) > 1:
        return

    alimento = self.tree_refeicao.item(self.selected_item, "values")[1]
    dieta = self.tree_refeicao.item(self.selected_item, "values")[2]
    self.combobox_alimento.set(alimento)
    self.combobox_alimento.config(foreground="black")
    self.combobox_dieta.set(dieta)
    self.combobox_dieta.config(foreground="black")

def info_treeview_refeicoesEdietas(self, tree):
    self.selected_item = self.tree_dietas.selection()

    a = self.tree_dietas.item(self.selected_item, "values")[1]

    resultado = pesquisar_join_bd("dim_refeicao", "dim_dieta", "dieta", "id_dieta", "nome", a)
    
    for i in resultado:
        alimento = valores_fatos("dim_alimento", "nome", "id_alimento", i[1])
        tree.insert("", "end", values=(alimento, i[3], i[4]))

    for i in resultado:
        nome_paciente = abrir_bd_fetchall("nome", "dim_usuario", "cpf", i[7])
        
        for j in nome_paciente:
            self.label_paciente.config(text=f"Paciente: {j[1]}")

##LOGIN
def cadastro_usuario(self):
    if self.entry_nome.get().isnumeric():
        showerror("ERRO", "Não insira números no campo de 'Nome'")
        return
    
    elif len(self.entry_cpf.get()) > 11:
        showerror("ERRO", "O campo 'CPF' está incorreto")
        return
    
    resultado = abrir_bd_fetchone("dim_usuario", "cpf", self.entry_cpf.get())
    if resultado:
        showerror("ERRO", "Ja existe um usuario com este cpf")
    
    for i in [self.entry_peso.get(), self.entry_altura.get()]:
    
        try:
            float(i)
    
        except ValueError:
            showerror("ERRO", "Insira apenas números para peso ou altura")
            return
        
    inserir_bd("dim_usuario", ("nome", "cpf", "altura", "peso", "tipo"), [self.entry_nome.get(), self.entry_cpf.get(), self.entry_peso.get(), self.entry_altura.get(), self.var.get()])

def fazer_login(tela, entry_usuario, entry_senha, tela_nutri, tela_paciente):
    resultado = abrir_bd_fetchall("nome, cpf, tipo", "dim_usuario", None, None)
    for i in resultado:
        if entry_usuario.get() == i[0] and int(entry_senha.get()) == i[1]:
            if i[2] == 1:
                cpf.append(entry_senha.get())
                tela.destroy()
                app = tela_nutri()
                app.mainloop()
            else:
                cpf.append(entry_senha.get())
                tela.destroy()
                app = tela_paciente()
                app.mainloop()
    else:
        print("erro")

##PACIENTE
def get_cpf(cpf, entry):
    cpf.append(int(entry.get()))

def info_treeview_paciente(self, tree):
    print(int(cpf[0]))
    resultado = pesquisar_join_bd("dim_refeicao", "dim_dieta", "dieta", "id_dieta", "cpf_paciente", int(cpf[0]))
    print(resultado)
    for i in resultado:
        alimento = valores_fatos("dim_alimento", "nome", "id_alimento", i[1])
        tree.insert("", "end", values=(alimento, i[3], i[4]))
        self.label_dieta.config(text=f"Dieta: {i[6]}")