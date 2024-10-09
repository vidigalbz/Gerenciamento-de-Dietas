from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import *
import mysql.connector

class Nutricionisa(Tk):
    def __init__(self, *args):
        super().__init__(*args)
        self.conexao = mysql.connector.connect(
            host = "localhost",
            user= "root",
            password = "acesso123",
            database = "gerenciamento_de_dietas",
                                              )
        self.cursor = self.conexao.cursor()
        self.start()
    
    ##FRONT-END
    def start(self):
        self.clear()
        self.title("NutryApp")
        self.geometry("1180x720")
        self.dashboard()
    
    def clear(self):
        for i in self.winfo_children():
            i.destroy()
        self.dashboard()
    
    def focus_entry(self, entry, text, color):
        if entry.get() == text:
            entry.delete(0, END)
            entry.config(fg=color)

    def Infocus_entry(self, entry, text, color):
        if entry.get() == "":
            entry.insert(0, text)
            entry.config(fg=color)

    def focus_combobox(self, combobox, text, color):
        if combobox.get() == text:
            combobox.set("") 
        combobox.config(foreground=color)

    def infocus_combobox(self, combobox, text, color):
        if combobox.get() == "":
            combobox.set(text)
            combobox.config(foreground=color)
    
    def dashboard(self):
        self.frame_dashboard = Frame(self, width=200, height=1080, bg="#007FFF")
        self.frame_dashboard.place(x=0, y=0)
        self.frame_dashboard.propagate(False)

        self.label_dashboard = Label(self.frame_dashboard, text="DASHBOARD", bg="#007FFF", fg="white", font=("Arial", 14, "bold"))
        self.label_dashboard.place(x=35, y=0)

        self.button_gerenciamentodedietas = Button(self.frame_dashboard, width=20, height=3, bg="white", text="Gerenciar Dietas", font=("Arial", 9, "bold"), command=self.gerenciamento_de_dietas)
        self.button_gerenciamentodedietas.place(x=25, y=250)

        self.button_alimentos = Button(self.frame_dashboard, width=20, height=3, bg="white", text="Alimentos", font=("Arial", 9, "bold"), command=self.alimentos)
        self.button_alimentos.place(x=25, y=320)

        self.button_planejamentoderefeicoes = Button(self.frame_dashboard, width=20, height=3, bg="white", text="Planejar Refeições", font=("Arial", 9, "bold"), command=self.planejamento_de_refeicoes)
        self.button_planejamentoderefeicoes.place(x=25, y=390)

    def gerenciamento_de_dietas(self):
        self.clear()
        self.button_alimentos.config(bg="white")
        self.button_planejamentoderefeicoes.config(bg="white")
        self.button_gerenciamentodedietas.config(bg="#00BFFF")

        self.button_start = Button(self, text="🏠", command=self.start, bg="white").place(x=200, y=0)

        Label(self, text="GERENCIAMENTO DE DIETAS", font=("Arial", 14, "bold")).place(x=550, y=30)

        self.entry_nome = Entry(self, width=25, fg="gray")
        self.entry_nome.place(x=250, y=75)
        self.entry_nome.insert(0, "Nome:")
        self.entry_nome.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_nome, "Nome:", "black"))
        self.entry_nome.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_nome, "Nome:", "gray"))

        self.entry_cpfpaciente = Entry(self, width=25, fg="gray")
        self.entry_cpfpaciente.place(x=450, y=75)
        self.entry_cpfpaciente.insert(0, "CPF Paciente: ")
        self.entry_cpfpaciente.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_cpfpaciente, "CPF Paciente: ", "black"))
        self.entry_cpfpaciente.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_cpfpaciente, "CPF Paciente: ", "gray"))
        
        self.entry_refeicoes = Entry(self, width=25, fg="gray")
        self.entry_refeicoes.place(x=650, y=75)
        self.entry_refeicoes.insert(0, "Refeições:")
        self.entry_refeicoes.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_refeicoes, "Refeições:", "black"))
        self.entry_refeicoes.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_refeicoes, "Refeições:", "gray"))

        self.entry_caloriasdiarias = Entry(self, width=25, fg="gray")
        self.entry_caloriasdiarias.place(x=850, y=75)
        self.entry_caloriasdiarias.insert(0, "Calorias Diárias:")
        self.entry_caloriasdiarias.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_caloriasdiarias, "Calorias Diárias:", "black"))
        self.entry_caloriasdiarias.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_caloriasdiarias, "Calorias Diárias:", "gray"))

        self.frame_pesquisa = Frame(self)
        self.frame_pesquisa.place(x=250, y=175)
        self.entry_pesquisa = Entry(self.frame_pesquisa, width=30)
        self.entry_pesquisa.grid(column=1, row=0)
        self.entry_pesquisa.insert(0, "Pesquisar:")
        self.entry_pesquisa.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_pesquisa, "Pesquisar:", "black"))
        self.entry_pesquisa.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_pesquisa, "Pesquisar:", "black"))

        filtro = ["ID", "Nome", "CPF", "Refeições", "Calorias Diárias", "Todos"]
        self.combobox_pesquisa = ttk.Combobox(self.frame_pesquisa, values=filtro, )
        self.combobox_pesquisa.set("Filtro")
        self.combobox_pesquisa.grid(column=0, row=0)
        self.combobox_pesquisa.config(state="readonly")

        self.button_cadastrar = Button(self, text="Cadastrar", bg="white", command=self.cadastrar_dieta, width=12)
        self.button_cadastrar.place(x=1035, y=72)

        self.button_editar = Button(self, text="Editar", bg="white", width=10, command=lambda: [self.editar_item(self.tree_dietas, self.button_cadastrar, [self.entry_nome, self.entry_cpfpaciente, self.entry_refeicoes, self.entry_caloriasdiarias], 1)])
        self.button_editar.place(x=965, y=667)

        self.button_remover = Button(self, text="Remover", bg="white", width=10, command=lambda: (self.remover_item(self.tree_dietas,  "dim_dieta", "id_dieta", 0)))
        self.button_remover.place(x=1047, y=667)

        self.tree_dietas = ttk.Treeview(self, columns=("ID", "Nome", "CPF do Paciente", "Refeições", "Calorias Diárias"), show="headings", height=22)
        self.tree_dietas.place(x=250, y=200)

        for i in ["ID", "Nome", "CPF do Paciente", "Refeições", "Calorias Diárias"]:
            self.tree_dietas.heading(f"{i}", text=f"{i}")

        for i in [("ID", 175), ("Nome", 175), ("CPF do Paciente", 175), ("Refeições", 175), ("Calorias Diárias", 175)]:
            self.tree_dietas.column(i[0], width=i[1], anchor="center")
        
        scrollbar = Scrollbar(self, orient=VERTICAL, command=self.tree_dietas.yview)
        scrollbar.place(x=1126, y=200, height=465)

        self.button_pesquisa = Button(self.frame_pesquisa, text="🔎", command=lambda: [self.pesquisar_item(self.tree_dietas, [("ID", "id_dieta"), ("Nome", "nome"), ("CPF", "cpf_paciente"), ("Refeições", "refeicoes"), ("Calorias Diárias", "calorias_diarias")], "dim_dieta", ["id_dieta", "nome", "cpf_paciente", "refeicoes", "calorias_diarias"], "dim_dieta")])
        self.button_pesquisa.grid(column=2, row=0)

        self.tree_dietas.configure(yscrollcommand=scrollbar.set)

        self.info_treeview(self.tree_dietas, "dim_dieta", None, None)

    def alimentos(self):
        self.clear()
        self.button_start = Button(self, text="🏠", command=self.start, bg="white").place(x=200, y=0)
        self.button_alimentos.config(bg="#00BFFF")
        self.button_planejamentoderefeicoes.config(bg="white")
        self.button_gerenciamentodedietas.config(bg="white")

        Label(self, text="CADASTRO DE ALIMENTOS", font=("Arial", 14, "bold")).place(x=550, y=30)
        
        self.entry_nome = Entry(self, width=21, fg="gray")
        self.entry_nome.place(x=250, y=75)
        self.entry_nome.insert(0, "Nome:")
        self.entry_nome.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_nome, "Nome:", "black"))
        self.entry_nome.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_nome, "Nome:", "gray"))

        self.entry_caloria = Entry(self, width=21, fg="gray")
        self.entry_caloria.place(x=410, y=75)
        self.entry_caloria.insert(0, "Calorias:")
        self.entry_caloria.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_caloria, "Calorias:", "black"))
        self.entry_caloria.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_caloria, "Calorias:", "gray"))

        self.entry_proteina = Entry(self, width=21, fg="gray")
        self.entry_proteina.place(x=570, y=75)
        self.entry_proteina.insert(0, "Proteínas:")
        self.entry_proteina.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_proteina, "Proteínas:", "black"))
        self.entry_proteina.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_proteina, "Proteínas:", "gray"))

        self.entry_carboidrato = Entry(self, width=21, fg="gray")
        self.entry_carboidrato.place(x=730, y=75)
        self.entry_carboidrato.insert(0, "Carboidratos:")
        self.entry_carboidrato.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_carboidrato, "Carboidratos:", "black"))
        self.entry_carboidrato.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_carboidrato, "Carboidratos:", "gray"))
        
        self.entry_gordura = Entry(self, width=21, fg="gray")
        self.entry_gordura.place(x=890, y=75)
        self.entry_gordura.insert(0, "Gorduras:")
        self.entry_gordura.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_gordura, "Gorduras:", "black"))
        self.entry_gordura.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_gordura, "Gorduras:", "gray"))

        self.button_cadastrar = Button(self, text="Cadastrar", bg="white", command=self.cadastrar_alimento, width=10)
        self.button_cadastrar.place(x=1047, y=72)

        self.frame_pesquisa = Frame(self)
        self.frame_pesquisa.place(x=250, y=175)
        self.entry_pesquisa = Entry(self.frame_pesquisa, width=30)
        self.entry_pesquisa.grid(column=1, row=0)
        self.entry_pesquisa.insert(0, "Pesquisar:")
        self.entry_pesquisa.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_pesquisa, "Pesquisar:", "black"))
        self.entry_pesquisa.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_pesquisa, "Pesquisar:", "black"))

        filtro = ["ID", "Nome", "Calorias", "Proteínas", "Carboidratos", "Gorduras", "Todos"]
        self.combobox_pesquisa = ttk.Combobox(self.frame_pesquisa, values=filtro, )
        self.combobox_pesquisa.set("Filtro")
        self.combobox_pesquisa.grid(column=0, row=0)
        self.combobox_pesquisa.config(state="readonly")

        self.button_editar = Button(self, text="Editar", bg="white", width=10, command=lambda: [self.editar_item(self.tree_alimentos, self.button_cadastrar, [self.entry_nome, self.entry_caloria, self.entry_proteina, self.entry_carboidrato, self.entry_gordura], 1)])
        self.button_editar.place(x=965, y=667)

        self.button_remover = Button(self, text="Remover", bg="white", width=10, command=lambda: (self.remover_item(self.tree_alimentos,  "dim_alimento", "id_alimento", 0)))
        self.button_remover.place(x=1047, y=667)

        self.tree_alimentos = ttk.Treeview(self, columns=("ID", "Nome", "Calorias", "Proteínas", "Carboidratos", "Gorduras"), show="headings", height=22)
        self.tree_alimentos.place(x=250, y=200)

        for i in ["ID", "Nome", "Calorias", "Proteínas", "Carboidratos", "Gorduras"]:
            self.tree_alimentos.heading(f"{i}", text=f"{i}")

        for i in [("ID", 146), ("Nome", 146), ("Calorias", 146), ("Proteínas", 146), ("Carboidratos", 146), ("Gorduras", 146)]:
            self.tree_alimentos.column(i[0], width=i[1], anchor="center")
        
        self.button_pesquisa = Button(self.frame_pesquisa, text="🔎", command=lambda: [self.pesquisar_item(self.tree_alimentos, [("ID", "id_alimento"), ("Nome", "nome"), ("Calorias", "caloria"), ("Proteínas", "proteina"), ("Carboidratos", "carboidrato"), ("Gorduras", "gordura")], "dim_alimento", ["id_alimento", "nome", "caloria", "proteina", "carboidrato", "gordura"], "dim_alimento")])
        self.button_pesquisa.grid(column=2, row=0)
        
        scrollbar = Scrollbar(self, orient=VERTICAL, command=self.tree_alimentos.yview)
        scrollbar.place(x=1126, y=200, height=465)

        self.tree_alimentos.configure(yscrollcommand=scrollbar.set)

        self.info_treeview(self.tree_alimentos, "dim_alimento", None, None)

    def planejamento_de_refeicoes(self):
        self.clear()
        self.button_start = Button(self, text="🏠", command=self.start, bg="white").place(x=200, y=0)
        self.button_alimentos.config(bg="white")
        self.button_planejamentoderefeicoes.config(bg="#00BFFF")
        self.button_gerenciamentodedietas.config(bg="white")

        opcoes = [opcao[0] for opcao in self.abrir_bd_fetchall("nome", "dim_alimento", None, None)]
        self.combobox_alimento = ttk.Combobox(self, values=opcoes, foreground="gray")
        self.combobox_alimento.set("Alimento:")
        self.combobox_alimento.place(x=250, y=75)
        self.combobox_alimento.bind("<FocusIn>", lambda event: self.focus_combobox(self.combobox_alimento, "Alimento:", "black"))
        self.combobox_alimento.bind("<FocusOut>", lambda event: self.infocus_combobox(self.combobox_alimento, "Alimento:", "gray"))

        opcoes = [opcao[0] for opcao in self.abrir_bd_fetchall("nome", "dim_dieta", None, None)]
        self.combobox_dieta = ttk.Combobox(self, values=opcoes, foreground="gray")
        self.combobox_dieta.set("Dieta:")
        self.combobox_dieta.place(x=450, y=75)
        self.combobox_dieta.bind("<FocusIn>", lambda event: self.focus_combobox(self.combobox_dieta, "Dieta", "black"))
        self.combobox_dieta.bind("<FocusOut>", lambda event: self.infocus_combobox(self.combobox_dieta, "Dieta", "gray"))

        self.entry_horario = Entry(self, width=21, fg="gray")
        self.entry_horario.place(x=650, y=75)
        self.entry_horario.insert(0, "Horário(00:00):")
        self.entry_horario.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_horario, "Horário(00:00):", "black"))
        self.entry_horario.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_horario, "Horário(00:00):", "gray"))

        self.entry_medida = Entry(self, width=21, fg="gray")
        self.entry_medida.place(x=850, y=75)
        self.entry_medida.insert(0, "Medida(KG):")
        self.entry_medida.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_medida, "Medida(KG):", "black"))
        self.entry_medida.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_medida, "Medida(KG):", "gray"))

        self.frame_pesquisa = Frame(self)
        self.frame_pesquisa.place(x=250, y=175)
        self.entry_pesquisa = Entry(self.frame_pesquisa, width=30)
        self.entry_pesquisa.grid(column=1, row=0)
        self.entry_pesquisa.insert(0, "Pesquisar:")
        self.entry_pesquisa.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_pesquisa, "Pesquisar:", "black"))
        self.entry_pesquisa.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_pesquisa, "Pesquisar:", "black"))

        filtro = ["ID", "Alimento", "Dieta", "Horário", "Medida", "Todos"]
        self.combobox_pesquisa = ttk.Combobox(self.frame_pesquisa, values=filtro, )
        self.combobox_pesquisa.set("Filtro")
        self.combobox_pesquisa.grid(column=0, row=0)
        self.combobox_pesquisa.config(state="readonly")

        self.button_cadastrar = Button(self, text="Cadastrar", bg="white", command=self.cadastrar_refeicao, width=12)
        self.button_cadastrar.place(x=1035, y=72)

        self.button_editar = Button(self, text="Editar", bg="white", width=10, command=lambda: [self.editar_combobox_refeicao(), self.editar_item(self.tree_refeicao, self.button_cadastrar, [self.entry_horario, self.entry_medida], 3)])
        self.button_editar.place(x=965, y=667)

        self.button_remover = Button(self, text="Remover", bg="white", width=10, command=lambda: (self.remover_item(self.tree_refeicao,  "dim_refeicao", "id_refeicao", 0)))
        self.button_remover.place(x=1047, y=667)

        self.tree_refeicao = ttk.Treeview(self, columns=("ID", "Alimento", "Dieta", "Horário", "Medida(KG)"), show="headings", height=22)
        self.tree_refeicao.place(x=250, y=200)

        for i in ["ID", "Alimento", "Dieta", "Horário", "Medida(KG)"]:
            self.tree_refeicao.heading(f"{i}", text=f"{i}")

        for i in [("ID", 175), ("Alimento", 175), ("Dieta", 175), ("Horário", 175), ("Medida(KG)", 175)]:
            self.tree_refeicao.column(i[0], width=i[1], anchor="center")
        
        scrollbar = Scrollbar(self, orient=VERTICAL, command=self.tree_refeicao.yview)
        scrollbar.place(x=1126, y=200, height=465)

        self.button_pesquisa = Button(self.frame_pesquisa, text="🔎", command=lambda: [self.pesquisar_item_join()])
        self.button_pesquisa.grid(column=2, row=0)

        self.tree_refeicao.configure(yscrollcommand=scrollbar.set)

        self.info_treeview_refeicao()

    ##BACK-END
    def info_treeview(self, tree, tabela, coluna, valor):
        resultado = self.abrir_bd_fetchall("*", tabela, coluna, valor)
        colunas = tree["columns"]

        for i in resultado:
        
            valores = i[:len(colunas)]
            tree.insert("", "end", values=valores)

    def remover_item(self, tree, tabela, coluna, index_info):
        selected_item = tree.selection()
        
        if not selected_item:
            showerror("ERRO", "Selecione um produto para usar esta função")
        
        else:
            yesno = askyesno("Confirmação", "Voce realmente deseja remover este(s) item?")
        
            if yesno:
                for i in selected_item:
                    valor = tree.item(i, "values")[index_info]
                    
                    self.delete_bd(tabela, coluna, valor) 
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
            resultado = self.pesquisar_tudo(tabela, columns, pesquisar_valor)
        for valor_pesquisa, coluna_bd in lista_de_tuplas:
            if valor == valor_pesquisa:
                resultado = self.like_bd(banco, coluna_bd, pesquisar_valor)
        
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
            resultado = self.pesquisar_join_bd("dim_refeicao", "dim_alimento", "alimento", "id_alimento", "nome", pesquisar_valor)
        
        elif valor == "Dieta":
            resultado = self.pesquisar_join_bd("dim_refeicao", "dim_dieta", "dieta", "id_dieta", "nome", pesquisar_valor)

        elif valor == "Filtro" or valor == "Todos":
            self.cursor.execute(""" SELECT * FROM dim_refeicao
                                    JOIN dim_alimento ON dim_refeicao.alimento = dim_alimento.id_alimento
                                    JOIN dim_dieta ON dim_refeicao.dieta = dim_dieta.id_dieta
                                    WHERE dim_alimento.nome LIKE %s
                                    AND dim_dieta.nome LIKE %s
                                    AND dim_refeicao.horario LIKE %s
                                    AND dim_refeicao.medida LIKE %s
                                    """, 
            (pesquisar_valor, pesquisar_valor, pesquisar_valor, pesquisar_valor))

            resultado = self.cursor.fetchall()
        
        for valor_pesquisa, coluna_bd in [("ID", "id_refeicao"),("Horário", "horario"), ("Medida", "medida")]:
            if valor == valor_pesquisa:
                resultado = self.like_bd("dim_refeicao", coluna_bd, pesquisar_valor)
        
        for item in self.tree_refeicao.get_children():
            self.tree_refeicao.delete(item)
        
        for i in resultado:
            alimento = self.valores_fatos("dim_alimento", "nome", "id_alimento", i[1])
            dieta = self.valores_fatos("dim_dieta", "nome", "id_dieta", i[2])
            self.tree_refeicao.insert("", "end", values=(i[0], alimento, dieta, i[3], i[4]))
    
    def cadastrar_dieta(self):
        resultado = self.abrir_bd_fetchone("dim_dieta", "cpf_paciente", self.entry_cpfpaciente.get())
            
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
                self.inserir_bd("dim_dieta", ["nome", "cpf_paciente", "refeicoes", "calorias_diarias"], (self.entry_nome.get(), self.entry_cpfpaciente.get(), self.entry_refeicoes.get(), self.entry_caloriasdiarias.get()))

        elif self.button_cadastrar.cget("text") == "Finalizar Edição":
            id_dieta = self.tree_dietas.item(self.selected_item, "values")[0]
     
            for coluna, valor in [("nome", self.entry_nome.get()), 
                                  ("cpf_paciente", self.entry_cpfpaciente.get()), 
                                  ("refeicoes", self.entry_refeicoes.get()), 
                                  ("calorias_diarias", self.entry_caloriasdiarias.get())]:
                    
                self.atualizar_bd(coluna, valor, "dieta", id_dieta)
            self.conexao.commit()
            
        else:
            showerror("ERRO", "Reinicie o aplicativo")

        for item in self.tree_dietas.get_children():
            self.tree_dietas.delete(item)
        
        self.info_treeview(self.tree_dietas, "dim_dieta", None, None)

        self.button_cadastrar.config(text="Cadastrar")
            

    def cadastrar_alimento(self):
        resultado = self.abrir_bd_fetchone("dim_alimento", "nome", self.entry_nome.get())

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
            
            self.inserir_bd("dim_alimento", ["nome", "caloria", "proteina", "carboidrato", "gordura"], (self.entry_nome.get(), self.entry_caloria.get(), self.entry_proteina.get(), self.entry_carboidrato.get(), self.entry_gordura.get()))
        
        elif self.button_cadastrar.cget("text") == "Finalizar Edição":
            id_alimento = self.tree_alimentos.item(self.selected_item, "values")[0]
                
            for coluna, valor in [("nome", self.entry_nome.get()), 
                                  ("caloria", self.entry_caloria.get()), 
                                  ("proteina", self.entry_proteina.get()), 
                                  ("carboidrato", self.entry_carboidrato.get()),
                                  ("gordura", self.entry_gordura.get())]:
                    
                self.atualizar_bd(coluna, valor, "alimento", id_alimento)
            self.conexao.commit()
            self.atualizar_bd(coluna, valor, "alimento", id_alimento)
        
        for item in self.tree_alimentos.get_children():
            self.tree_alimentos.delete(item)

        self.info_treeview(self.tree_alimentos, "dim_alimento", None, None)

        self.button_cadastrar.config(text="Cadastrar")
    
    def cadastrar_refeicao(self):
        id_alimento = self.valores_fatos("dim_alimento", "id_alimento", "nome", self.combobox_alimento.get())
        id_dieta = self.valores_fatos("dim_dieta", "id_dieta", "nome", self.combobox_dieta.get())

        if id_alimento == "None" or id_dieta == "None":
            showerror("ERRO", "Dieta ou Alimento nao existentes")
            return
        
        if self.button_cadastrar.cget("text") == "Cadastrar":
            self.inserir_bd("dim_refeicao", ["alimento", "dieta", "horario", "medida"], (id_alimento, id_dieta, self.entry_horario.get(), self.entry_medida.get()))
        
        elif self.button_cadastrar.cget("text") == "Finalizar Edição":
            id_refeicao = self.tree_refeicao.item(self.selected_item, "values")[0]

            for coluna, valor in [("alimento", id_alimento),
                                  ("dieta", id_dieta),
                                  ("horario", self.entry_horario.get()),
                                  ("medida", self.entry_medida.get())]:
                self.atualizar_bd(coluna, valor, "refeicao", id_refeicao)
            self.conexao.commit()

        for item in self.tree_refeicao.get_children():
            self.tree_refeicao.delete(item)
        
        self.info_treeview_refeicao()
        
        self.button_cadastrar.config(text="Cadastrar")
    
    def info_treeview_refeicao(self):
        resultado = self.abrir_bd_fetchall("*", "dim_refeicao", None, None)

        for i in resultado:
            id_alimento = self.valores_fatos("dim_alimento", "nome", "id_alimento", i[1])
            id_dieta = self.valores_fatos("dim_dieta", "nome", "id_dieta", i[2])

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

    ##MYSQL
    def abrir_bd_fetchall(self, tipo, table, coluna, valor):
        if coluna == None:    
            self.cursor.execute("SELECT "+ tipo +" FROM "+ table)
            resultado = self.cursor.fetchall()
            return resultado
        
        else:
            self.cursor.execute("SELECT * FROM " + table +" WHERE " + coluna +"= %s", (valor,))
            resultado = self.cursor.fetchall()
            return resultado
            
    def abrir_bd_fetchone(self, table, coluna, valor):
        self.cursor.execute("SELECT * FROM "+ table + " WHERE " + coluna + "= %s", (valor, ))
        resultado = self.cursor.fetchone()
        return resultado
    
    def delete_bd(self, tabela, coluna, valor):
        self.cursor.execute("DELETE FROM " + tabela + " WHERE "+ coluna +"= %s", (valor, ))
        self.conexao.commit()
     
    def like_bd(self, table, coluna, valor):
        self.cursor.execute("SELECT * FROM " + table + " WHERE "+ coluna + " LIKE %s", (valor, ))
        resultado = self.cursor.fetchall()
        return resultado
   
    def pesquisar_join_bd(self, table, table2, coluna, coluna2, coluna3, valor):
        self.cursor.execute(f"SELECT * FROM {table} JOIN {table2} ON {table}.{coluna} = {table2}.{coluna2} WHERE {table2}.{coluna3} LIKE %s", (valor, ))
        resultado = self.cursor.fetchall()
        return resultado
    
    def atualizar_bd(self, coluna, valor_coluna, id, valor_id):
        self.cursor.execute("UPDATE dim_" + id + " SET " + coluna + "=%s WHERE id_" + id + "=%s", (valor_coluna, valor_id))
        self.conexao.commit()

    def valores_fatos(self, tabela, coluna, coluna2, valor):
        self.cursor.execute("SELECT " + coluna + " FROM " + tabela + " WHERE " + coluna2 + "= %s", (valor, ))
        resultado = self.cursor.fetchone()
        
        if resultado:
            for i in resultado:
                return i
            
    def pesquisar_tudo(self, tabela, colunas, valor):
        self.cursor.execute(f"SELECT * FROM {tabela} WHERE " + " OR ".join([f"{coluna} LIKE %s" for coluna in colunas]), tuple([valor] * len(colunas)))
        resultado = self.cursor.fetchall()  
        return resultado

    def inserir_bd(self, table, columns, values):
        colunas = ", ".join(columns)
        valores = ", ".join(["%s"] * len(values))     
        self.cursor.execute(f"INSERT INTO {table}({colunas}) VALUES({valores})",values)
        self.conexao.commit()

if __name__ == "__main__":
    app = Nutricionisa()
    app.mainloop()