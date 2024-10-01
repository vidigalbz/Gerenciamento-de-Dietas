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

    def start(self):
        self.title("Dashboard")
        self.geometry("1180x720")
        self.dashboard()
    
    def clear(self):
        for i in self.winfo_children():
            i.destroy()
        self.dashboard()

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

        self.entry_nome = Entry(self, width=25)
        self.entry_nome.place(x=250, y=50)
        self.entry_nome.insert(0, "Nome:")

        self.entry_cpfpasciente = Entry(self, width=25)
        self.entry_cpfpasciente.place(x=450, y=50)
        self.entry_cpfpasciente.insert(0, "CPF Pasciente:")

        self.entry_refeicoes = Entry(self, width=25)
        self.entry_refeicoes.place(x=650, y=50)
        self.entry_refeicoes.insert(0, "Refeições:")

        self.entry_caloriasdiarias = Entry(self, width=25)
        self.entry_caloriasdiarias.place(x=850, y=50)
        self.entry_caloriasdiarias.insert(0, "Calorias Diarias:")

        self.frame_pesquisa = Frame(self)
        self.frame_pesquisa.place(x=200, y=175)
        self.entry_pesquisa = Entry(self.frame_pesquisa, width=30)
        self.entry_pesquisa.grid(column=1, row=0)
        self.entry_pesquisa.insert(0, "Pesquisar:")
        self.button_pesquisa = Button(self.frame_pesquisa, text="🔎", command=None)
        self.button_pesquisa.grid(column=2, row=0)
        
        filtro = ["Nome", "CPF", "Refeições", "Calorias"]
        self.combobox_pesquisa = ttk.Combobox(self.frame_pesquisa, values=filtro)
        self.combobox_pesquisa.set("Filtro")
        self.combobox_pesquisa.grid(column=0, row=0)

        self.button_cadastrar = Button(self, text="Cadastrar", bg="white", command=None, width=10)
        self.button_cadastrar.place(x=1050, y=45)

        self.tree_dietas = ttk.Treeview(self, columns=("ID", "Nome", "CPF do Pasciente", "Refeições", "Calorias Diarias"), show="headings", height=22)
        self.tree_dietas.place(x=250, y=200)

        for i in ["ID", "Nome", "CPF do Pasciente", "Refeições", "Calorias Diarias"]:
            self.tree_dietas.heading(f"{i}", text=f"{i}")

        for i in [("ID", 175), ("Nome", 175), ("CPF do Pasciente", 175), ("Refeições", 175), ("Calorias Diarias", 175)]:
            self.tree_dietas.column(i[0], width=i[1], anchor="center")

    def alimentos(self):
        self.clear()
        self.button_alimentos.config(bg="#00BFFF")
        self.button_planejamentoderefeicoes.config(bg="white")
        self.button_gerenciamentodedietas.config(bg="white")
    
    def planejamento_de_refeicoes(self):
        self.clear()
        self.button_alimentos.config(bg="white")
        self.button_planejamentoderefeicoes.config(bg="#00BFFF")
        self.button_gerenciamentodedietas.config(bg="white")

if __name__ == "__main__":
    app = Nutricionisa()
    app.mainloop()