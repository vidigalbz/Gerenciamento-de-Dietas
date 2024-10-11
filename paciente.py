from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import *
from bd import *
from backend import *

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

        self.tree_paciente = ttk.Treeview(self, columns=("Alimento", "Horário", "Medida(KG)"), show="headings", height=22)
        self.tree_paciente.place(x=300, y=150)

        for i in ["Alimento", "Horário", "Medida(KG)"]:
            self.tree_paciente.heading(f"{i}", text=f"{i}")

        for i in [("Alimento", 200), ("Horário", 200), ("Medida(KG)", 200)]:
            self.tree_paciente.column(i[0], width=i[1], anchor="center")

        info_treeview_paciente(self, self.tree_paciente)

if __name__ == "__main__":
    app = Paciente()
    app.mainloop()
