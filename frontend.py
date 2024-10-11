from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import *
from bd import *
from backend import *

cpf = []

##Login Screen
class Login(Tk):
    def __init__(self, *args):
        super().__init__(*args)
        self.login()

    def clear(self):
        for i in self.winfo_children():
            i.destroy()

    def login(self):
        self.title('Login')
        self.geometry('500x400')

        Label(self, text="LOGIN", font=("Arial", 12, "bold")).pack(padx=10, pady=10)

        self.label_nome = Label(self, text='Usuario:')
        self.label_nome.pack()
        self.entry_nome = Entry(self, width=30)
        self.entry_nome.pack(pady=5)
    
        self.label_password = Label(self, text='Senha:')
        self.label_password.pack()
        self.entry_password = Entry(self, show='*', width=30)
        self.entry_password.pack(pady=5)
    
        self.frame_buttons = Frame(self)
        self.frame_buttons.pack(pady=20)

        self.button_login = Button(self.frame_buttons, text='Login', width=10, command=lambda: [get_cpf(cpf, self.entry_password), fazer_login(self, self.entry_nome, self.entry_password, Nutricionisa, Paciente)], bg="white")
        self.button_login.pack(side=LEFT, padx=10)
    
        self.button_cancel = Button(self.frame_buttons, text='Cancelar', width=10, command=self.quit, bg="white")
        self.button_cancel.pack(side=RIGHT, padx=10)

        self.label_cadastrar = Label(self, text="Cadastrar-se", fg="skyblue")
        self.label_cadastrar.pack()
        self.label_cadastrar.bind("<Button>", self.cadastro)

    def cadastro(self, event=None):
        self.clear()
        self.geometry("500x600")

        Label(self, text="CADASTRO", font=("Arial", 12, "bold")).pack(padx=10, pady=10)
        self.label_nome = Label(self, text='Nome:')
        self.label_nome.pack()
        self.entry_nome = Entry(self, width=30)
        self.entry_nome.pack(pady=5)

        self.label_cpf = Label(self, text='CPF: ')
        self.label_cpf.pack()
        self.entry_cpf = Entry(self, width=30)
        self.entry_cpf.pack(pady=5)

        self.label_peso = Label(self, text='Peso: ')
        self.label_peso.pack()
        self.entry_peso = Entry(self, width=30)
        self.entry_peso.pack(pady=5)

        self.label_altura = Label(self, text="Altura: ")
        self.label_altura.pack()
        self.entry_altura = Entry(self, width=30)
        self.entry_altura.pack(pady=5)

        self.framebutton = Frame(self)
        self.framebutton.pack(pady=10)

        self.var = IntVar()
        self.var.set(0)
        self.radionbutton_frame = Frame(self)
        self.radionbutton_frame.pack()        
        self.radio_nutricionistaa = Radiobutton(self.radionbutton_frame, text="Nutricionista", value=1, variable=self.var)
        self.radio_paciente = Radiobutton(self.radionbutton_frame, text="Paciente", value=2, variable=self.var)
        self.radio_nutricionistaa.pack()
        self.radio_paciente.pack()
        
        self.button_cadastrar = Button(self, text='Cadastrar', width=20, command=lambda: [cadastro_usuario(self)], bg="white")
        self.button_cadastrar.pack(padx=10, pady=10)
    
        self.botao_cancelar = Button(self, text='Cancelar', width=20, command=lambda: [self.clear(), self.login()], bg="white")
        self.botao_cancelar.pack(padx=10, pady=10)

##Nutri Screen
class Nutricionisa(Tk):
    def __init__(self, *args):
        super().__init__(*args)
        self.start()
    
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
        Label(self, text="BEM-VINDO!", font=("Arial", 17, "bold")).place(x=600, y=30)

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

        self.button_cadastrar = Button(self, text="Cadastrar", bg="white", command=lambda: [cadastrar_dieta(self)], width=12)
        self.button_cadastrar.place(x=1035, y=72)

        self.button_editar = Button(self, text="Editar", bg="white", width=10, command=lambda: [editar_item(self, self.tree_dietas, self.button_cadastrar, [self.entry_nome, self.entry_cpfpaciente, self.entry_refeicoes, self.entry_caloriasdiarias], 1)])
        self.button_editar.place(x=965, y=667)

        self.button_remover = Button(self, text="Remover", bg="white", width=10, command=lambda: [remover_item(self.tree_dietas,  "dim_dieta", "id_dieta", 0)])
        self.button_remover.place(x=1047, y=667)

        self.button_refeicoes = Button(self, text="Ver Refeições", bg="white", width=10, command=lambda: [self.ver_refeicoes()])
        self.button_refeicoes.place(x=250, y=667)

        self.tree_dietas = ttk.Treeview(self, columns=("ID", "Nome", "CPF do Paciente", "Refeições", "Calorias Diárias"), show="headings", height=22)
        self.tree_dietas.place(x=250, y=200)

        for i in ["ID", "Nome", "CPF do Paciente", "Refeições", "Calorias Diárias"]:
            self.tree_dietas.heading(f"{i}", text=f"{i}")

        for i in [("ID", 175), ("Nome", 175), ("CPF do Paciente", 175), ("Refeições", 175), ("Calorias Diárias", 175)]:
            self.tree_dietas.column(i[0], width=i[1], anchor="center")
        
        scrollbar = Scrollbar(self, orient=VERTICAL, command=self.tree_dietas.yview)
        scrollbar.place(x=1126, y=200, height=465)

        self.button_pesquisa = Button(self.frame_pesquisa, text="🔎", command=lambda: [pesquisar_item(self, self.tree_dietas, [("ID", "id_dieta"), ("Nome", "nome"), ("CPF", "cpf_paciente"), ("Refeições", "refeicoes"), ("Calorias Diárias", "calorias_diarias")], "dim_dieta", ["id_dieta", "nome", "cpf_paciente", "refeicoes", "calorias_diarias"], "dim_dieta")])
        self.button_pesquisa.grid(column=2, row=0)

        self.tree_dietas.configure(yscrollcommand=scrollbar.set)

        info_treeview(self.tree_dietas, "dim_dieta", None, None)

    def alimentos(self):
        self.clear()
        self.button_start = Button(self, text="🏠", command=self.start, bg="white").place(x=200, y=0)
        self.button_alimentos.config(bg="#00BFFF")
        self.button_planejamentoderefeicoes.config(bg="white")
        self.button_gerenciamentodedietas.config(bg="white")

        Label(self, text="CADASTRO DE ALIMENTOS", font=("Arial", 14, "bold")).place(x=550, y=30)
        Label(self, text="MEDIDA PADRÃO: 100g", font=("Arial", 8, "bold")).place(x=250, y=667)
        
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

        self.button_cadastrar = Button(self, text="Cadastrar", bg="white", command=lambda: [cadastrar_alimento(self)], width=10)
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

        self.button_editar = Button(self, text="Editar", bg="white", width=10, command=lambda: [editar_item(self, self.tree_alimentos, self.button_cadastrar, [self.entry_nome, self.entry_caloria, self.entry_proteina, self.entry_carboidrato, self.entry_gordura], 1)])
        self.button_editar.place(x=965, y=667)

        self.button_remover = Button(self, text="Remover", bg="white", width=10, command=lambda: (remover_item(self.tree_alimentos,  "dim_alimento", "id_alimento", 0)))
        self.button_remover.place(x=1047, y=667)

        self.tree_alimentos = ttk.Treeview(self, columns=("ID", "Nome", "Calorias", "Proteínas", "Carboidratos", "Gorduras"), show="headings", height=22)
        self.tree_alimentos.place(x=250, y=200)

        for i in ["ID", "Nome", "Calorias", "Proteínas", "Carboidratos", "Gorduras"]:
            self.tree_alimentos.heading(f"{i}", text=f"{i}")

        for i in [("ID", 146), ("Nome", 146), ("Calorias", 146), ("Proteínas", 146), ("Carboidratos", 146), ("Gorduras", 146)]:
            self.tree_alimentos.column(i[0], width=i[1], anchor="center")
        
        self.button_pesquisa = Button(self.frame_pesquisa, text="🔎", command=lambda: [pesquisar_item(self, self.tree_alimentos, [("ID", "id_alimento"), ("Nome", "nome"), ("Calorias", "caloria"), ("Proteínas", "proteina"), ("Carboidratos", "carboidrato"), ("Gorduras", "gordura")], "dim_alimento", ["id_alimento", "nome", "caloria", "proteina", "carboidrato", "gordura"], "dim_alimento")])
        self.button_pesquisa.grid(column=2, row=0)
        
        scrollbar = Scrollbar(self, orient=VERTICAL, command=self.tree_alimentos.yview)
        scrollbar.place(x=1126, y=200, height=465)

        self.tree_alimentos.configure(yscrollcommand=scrollbar.set)

        info_treeview(self.tree_alimentos, "dim_alimento", None, None)

    def planejamento_de_refeicoes(self):
        self.clear()
        self.button_start = Button(self, text="🏠", command=self.start, bg="white").place(x=200, y=0)
        self.button_alimentos.config(bg="white")
        self.button_planejamentoderefeicoes.config(bg="#00BFFF")
        self.button_gerenciamentodedietas.config(bg="white")

        Label(self, text="PLANEJAMENTO DE REFEIÇÕES", font=("Arial", 14, "bold")).place(x=550, y=30)

        opcoes = [opcao[0] for opcao in abrir_bd_fetchall("nome", "dim_alimento", None, None)]
        self.combobox_alimento = ttk.Combobox(self, values=opcoes, foreground="gray")
        self.combobox_alimento.set("Alimento:")
        self.combobox_alimento.place(x=250, y=75)
        self.combobox_alimento.bind("<FocusIn>", lambda event: self.focus_combobox(self.combobox_alimento, "Alimento:", "black"))
        self.combobox_alimento.bind("<FocusOut>", lambda event: self.infocus_combobox(self.combobox_alimento, "Alimento:", "gray"))

        opcoes = [opcao[0] for opcao in abrir_bd_fetchall("nome", "dim_dieta", None, None)]
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
        self.entry_medida.insert(0, "Medida(G):")
        self.entry_medida.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_medida, "Medida(G):", "black"))
        self.entry_medida.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_medida, "Medida(G):", "gray"))

        self.frame_pesquisa = Frame(self)
        self.frame_pesquisa.place(x=250, y=175)
        self.entry_pesquisa = Entry(self.frame_pesquisa, width=30)
        self.entry_pesquisa.grid(column=1, row=0)
        self.entry_pesquisa.insert(0, "Pesquisar:")
        self.entry_pesquisa.bind("<FocusIn>", lambda event: self.focus_entry(self.entry_pesquisa, "Pesquisar:", "black"))
        self.entry_pesquisa.bind("<FocusOut>", lambda event: self.Infocus_entry(self.entry_pesquisa, "Pesquisar:", "black"))

        filtro = ["ID", "Alimento", "Dieta", "Horário", "Medida"]
        self.combobox_pesquisa = ttk.Combobox(self.frame_pesquisa, values=filtro, )
        self.combobox_pesquisa.set("Filtro")
        self.combobox_pesquisa.grid(column=0, row=0)
        self.combobox_pesquisa.config(state="readonly")

        self.button_cadastrar = Button(self, text="Cadastrar", bg="white", command=lambda: [cadastrar_refeicao(self)], width=12)
        self.button_cadastrar.place(x=1035, y=72)

        self.button_editar = Button(self, text="Editar", bg="white", width=10, command=lambda: [editar_combobox_refeicao(self), editar_item(self, self.tree_refeicao, self.button_cadastrar, [self.entry_horario, self.entry_medida], 3)])
        self.button_editar.place(x=965, y=667)

        self.button_remover = Button(self, text="Remover", bg="white", width=10, command=lambda: (remover_item(self.tree_refeicao,  "dim_refeicao", "id_refeicao", 0)))
        self.button_remover.place(x=1047, y=667)

        self.tree_refeicao = ttk.Treeview(self, columns=("ID", "Alimento", "Dieta", "Horário", "Medida(G)"), show="headings", height=22)
        self.tree_refeicao.place(x=250, y=200)

        for i in ["ID", "Alimento", "Dieta", "Horário", "Medida(G)"]:
            self.tree_refeicao.heading(f"{i}", text=f"{i}")

        for i in [("ID", 175), ("Alimento", 175), ("Dieta", 175), ("Horário", 175), ("Medida(G)", 175)]:
            self.tree_refeicao.column(i[0], width=i[1], anchor="center")
        
        scrollbar = Scrollbar(self, orient=VERTICAL, command=self.tree_refeicao.yview)
        scrollbar.place(x=1126, y=200, height=465)

        self.button_pesquisa = Button(self.frame_pesquisa, text="🔎", command=lambda: [pesquisar_item_join(self)])
        self.button_pesquisa.grid(column=2, row=0)

        self.tree_refeicao.configure(yscrollcommand=scrollbar.set)

        info_treeview_refeicao(self)

    def ver_refeicoes(self):
        screen_ref = Tk()
        screen_ref.geometry("982x750")
        screen_ref.title("Plano de Refeição")

        self.button_voltar = Button(screen_ref, text="<< Voltar", command=screen_ref.destroy, bg="white")
        self.button_voltar.place(x=0, y=0)

        Label(screen_ref, text="PLANO DE REFEIÇÃO", font=("Arial", 17, "bold")).pack()
        self.label_paciente = Label(screen_ref, text="Paciente: ", font="Arial")
        self.label_paciente.place(x=190, y=60)

        self.tree_refeicao_e_dieta = ttk.Treeview(screen_ref, columns=("Refeição", "Horário", "Medida(G)"), show="headings", height=22)
        self.tree_refeicao_e_dieta.pack(pady=100)

        for i in ["Refeição", "Horário", "Medida(G)"]:
            self.tree_refeicao_e_dieta.heading(f"{i}", text=f"{i}")

        for i in [("Refeição", 200), ("Horário", 200), ("Medida(G)", 200)]:
            self.tree_refeicao_e_dieta.column(i[0], width=i[1], anchor="center")

        scrollbar = Scrollbar(screen_ref, orient=VERTICAL, command=self.tree_refeicao_e_dieta.yview)
        scrollbar.place(x=790, y=133, height=465)
        info_treeview_refeicoesEdietas(self, self.tree_refeicao_e_dieta)
        screen_ref.mainloop()


##PACIENTE  
class Paciente(Tk):
    def __init__(self, *args):
        super().__init__(*args)
        self.start()
    
    def start(self):
        self.clear()
        self.title("NutryApp")
        self.geometry("1180x720")
        self.dashboard()
        
    def clear(self):
        for i in self.winfo_children():
            i.destroy()

    def dashboard(self):
        Label(self, text="BEM-VINDO!", font=("Arial", 18, "bold")).pack(padx=15, pady=15)
        self.label_dieta = Label(self, text="Minha Dieta: ", font="bold")
        self.label_dieta.place(x=200, y=75)

        self.tree_paciente = ttk.Treeview(self, columns=("Alimento", "Horário", "Medida(G)"), show="headings", height=22)
        self.tree_paciente.place(x=300, y=150)

        for i in ["Alimento", "Horário", "Medida(G)"]:
            self.tree_paciente.heading(f"{i}", text=f"{i}")

        for i in [("Alimento", 200), ("Horário", 200), ("Medida(G)", 200)]:
            self.tree_paciente.column(i[0], width=i[1], anchor="center")

        info_treeview_paciente(self, self.tree_paciente)

if __name__ == "__main__":
    app = Login()
    app.mainloop()