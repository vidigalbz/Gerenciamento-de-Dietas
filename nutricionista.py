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
        self.title("Dashboard")
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
        self.button_pesquisa = Button(self.frame_pesquisa, text="🔎", command=self.pesquisar)
        self.button_pesquisa.grid(column=2, row=0)

        filtro = ["ID", "Nome", "CPF", "Refeições", "Calorias Diárias", "Todos"]
        self.combobox_pesquisa = ttk.Combobox(self.frame_pesquisa, values=filtro, )
        self.combobox_pesquisa.set("Filtro")
        self.combobox_pesquisa.grid(column=0, row=0)
        self.combobox_pesquisa.config(state="readonly")

        self.button_cadastrar = Button(self, text="Cadastrar", bg="white", command=self.cadastrar_dieta, width=12)
        self.button_cadastrar.place(x=1035, y=72)

        self.button_editar = Button(self, text="Editar", bg="white", width=10, command=lambda: [self.editar_item_dietas()])
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
        self.button_pesquisa = Button(self.frame_pesquisa, text="🔎", command=self.pesquisar)
        self.button_pesquisa.grid(column=2, row=0)

        filtro = ["ID", "Nome", "Calorias", "Proteínas", "Carboidratos", "Gorduras", "Todos"]
        self.combobox_pesquisa = ttk.Combobox(self.frame_pesquisa, values=filtro, )
        self.combobox_pesquisa.set("Filtro")
        self.combobox_pesquisa.grid(column=0, row=0)
        self.combobox_pesquisa.config(state="readonly")

        self.button_editar = Button(self, text="Editar", bg="white", width=10, command=lambda: [self.editar_item_dietas()])
        self.button_editar.place(x=965, y=667)

        self.button_remover = Button(self, text="Remover", bg="white", width=10, command=lambda: (self.remover_item(self.tree_alimentos,  "dim_alimento", "id_alimento", 0)))
        self.button_remover.place(x=1047, y=667)

        self.tree_alimentos = ttk.Treeview(self, columns=("ID", "Nome", "Calorias", "Proteínas", "Carboidratos", "Gorduras"), show="headings", height=22)
        self.tree_alimentos.place(x=250, y=200)

        for i in ["ID", "Nome", "Calorias", "Proteínas", "Carboidratos", "Gorduras"]:
            self.tree_alimentos.heading(f"{i}", text=f"{i}")

        for i in [("ID", 146), ("Nome", 146), ("Calorias", 146), ("Proteínas", 146), ("Carboidratos", 146), ("Gorduras", 146)]:
            self.tree_alimentos.column(i[0], width=i[1], anchor="center")
        
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

    ##BACK-END
    def info_treeview(self, tree, tabela, coluna, valor):
        resultado = self.abrir_bd_fetchall(tabela, coluna, valor)
        for i in resultado:
            tree.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4]))

    def cadastrar_dieta(self):
            resultado = self.abrir_bd_fetchone("dim_dieta", "cpf_paciente", self.entry_cpfpaciente.get())
            
            if [self.entry_nome.get(), self.entry_cpfpaciente.get(), self.entry_refeicoes.get(), self.entry_caloriasdiarias.get()] == "":
                showerror("ERRO", "Preencha todos os campos para fazer cadastro")
                return
                
            elif not self.entry_cpfpaciente.get().isnumeric():
                showerror("ERRO",  "Insira apenas números no campo 'CPF Paciente'")
                return
            
            elif not self.entry_refeicoes.get().isnumeric():
                showerror("ERRO",  "Insira apenas números no campo 'Refeições'")
                return
            
            elif not self.entry_caloriasdiarias.get().isnumeric():
                showerror("ERRO",  "Insira apenas números no campo 'Calorias Diárias'")
                return

            elif len(self.entry_cpfpaciente.get()) > 11 or len(self.entry_cpfpaciente.get()) < 11:
                showerror("ERRO", "O campo 'CPF Paciente' está incorreto")
                return

            try:
                float(self.entry_caloriasdiarias.get())

            except ValueError:
                showerror("ERRO", "Insira apenas números no campo 'Calorias Diárias'")


            if self.button_cadastrar.cget("text") == "Cadastrar":                
                if resultado:
                    showerror("ERRO", "Já existe uma dieta com este cpf")

                else:    
                    self.inserir_dieta_bd()

        
            elif self.button_cadastrar.cget("text") == "Finalizar Edição":
                id_dieta = self.tree_dietas.item(self.selected_item, "values")[0]
                
                for coluna, valor in [("nome", self.entry_nome.get()), 
                                      ("cpf_paciente", self.entry_cpfpaciente.get()), 
                                      ("refeicoes", self.entry_refeicoes.get()), 
                                      ("calorias_diarias", self.entry_caloriasdiarias.get())]:
                    
                    self.atualizar_dieta_bd(coluna, valor, id_dieta)
                self.conexao.commit()
            
            else:
                showerror("ERRO", "Reinicie o aplicativo")

            for item in self.tree_dietas.get_children():
                        self.tree_dietas.delete(item)
                
            self.info_treeview(self.tree_dietas, "dim_dieta", None, None)
            
            self.button_cadastrar.config(text="Cadastrar")

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
    
    def pesquisar(self):
        valor = self.combobox_pesquisa.get()
        pesquisar = f"{self.entry_pesquisa.get()}%"

        if valor == "Filtro" or valor == "Todos":
            resultado = self.pesquisar_tudo_dietas(pesquisar)

        elif valor == "ID":
            resultado = self.like_bd("dim_dieta", "id_dieta", pesquisar)    

        elif valor == "Nome":
            resultado = self.like_bd("dim_dieta", "nome", pesquisar)
        
        elif valor == "CPF":
            resultado = self.like_bd("dim_dieta", "cpf_paciente", pesquisar)
        
        elif valor == "Refeições":
            resultado = self.like_bd("dim_dieta", "refeicoes", pesquisar)
        
        elif valor == "Calorias Diarias":
            resultado = self.like_bd("dim_dieta", "calorias_diarias", pesquisar)
        
        for item in self.tree_dietas.get_children():
            self.tree_dietas.delete(item)
        
        for i in resultado:
            self.tree_dietas.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4]))
    

    def editar_item_dietas(self):
        self.selected_item = self.tree_dietas.selection()

        if not self.selected_item:
            showerror("ERRO", "Selecione um produto para usar esta função")
        
        elif len(self.selected_item) > 1:
            showerror("ERRO", "Não é possivel editar mais de um item de uma vez")
        
        else:
            self.button_cadastrar.config(text="Finalizar Edição")
            info = []

            for i in range(1, 5):
                infos = self.tree_dietas.item(self.selected_item, "values")[i]
                info.append(infos)

            for entry, new_info in [(self.entry_nome, info[0]), 
                                    (self.entry_cpfpaciente, info[1]),
                                    (self.entry_refeicoes, info[2]),
                                    (self.entry_caloriasdiarias, info[3])]:
                            
                entry.delete(0, END)
                entry.insert(0, new_info)
                entry.configure(fg="black")
    
    def cadastrar_alimento(self):
        resultado = self.abrir_bd_fetchone("dim_dieta", "nome", self.entry_nome.get())

        if resultado:
            showerror("ERRO", "Este alimento ja existe no sistema")
        
        for i in [self.entry_caloria.get(), self.entry_carboidrato.get(), self.entry_gordura.get(), self.entry_proteina.get()]:
            try:
                float(i)
            except ValueError:
                showerror("ERRO", "Insira apenas valores numericos nos campos de valores")
        
        for i in [self.entry_caloria, self.entry_carboidrato, self.entry_gordura, self.entry_proteina]:
            if not i.get().isnumeric():
                showerror("ERRO", f"Insira apenas valores numericos nos campos de valores")
                return
            
        
        if self.button_cadastrar.cget("text") == "Cadastrar":
            self.inserir_alimento_bd()
            self.info_treeview(self.tree_alimentos, "dim_alimento", None, None)

    ##MYSQL
    def abrir_bd_fetchall(self, table, coluna, valor):
        if coluna == None:    
            self.cursor.execute("SELECT * FROM "+ table)
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
   
    def inserir_dieta_bd(self):
        self.cursor.execute("INSERT INTO dim_dieta(nome, cpf_paciente, refeicoes, calorias_diarias) VALUES(%s, %s, %s, %s)", (self.entry_nome.get(), self.entry_cpfpaciente.get(), self.entry_refeicoes.get(), self.entry_caloriasdiarias.get()))
        self.conexao.commit()
    
    def atualizar_dieta_bd(self, coluna, valor_coluna, valor_id):
        self.cursor.execute("UPDATE dim_dieta SET " + coluna + "=%s WHERE id_dieta =%s", (valor_coluna, valor_id))
        self.conexao.commit()
    
    def pesquisar_tudo_dietas(self, valor):
        self.cursor.execute("""
        SELECT * FROM dim_dieta WHERE id_dieta LIKE %s or 
        nome LIKE %s or 
        cpf_paciente LIKE %s or
        refeicoes LIKE %s or
        calorias_diarias LIKE %s
        """, (valor, valor, valor, valor, valor))
        resultado = self.cursor.fetchall()
        return resultado
    
    def inserir_alimento_bd(self):
        self.cursor.execute("INSERT INTO dim_alimento(nome, caloria, proteina, carboidrato, gordura) VALUES(%s, %s, %s, %s, %s)", (self.entry_nome.get(), self.entry_caloria.get(), self.entry_proteina.get(), self.entry_carboidrato.get(), self.entry_gordura.get()))
        self.conexao.commit()

if __name__ == "__main__":
    app = Nutricionisa()
    app.mainloop()