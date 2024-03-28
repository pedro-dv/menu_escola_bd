from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from aluno import Aluno
from aluno_banco import AlunoBanco


class App:
    def __init__(self):
        self.db = AlunoBanco('localhost', 'root', 'escola', '')


        self.janela = Tk()
        self.janela.title('SysAlunos')

        # Label
        self.label_matricula = Label(self.janela, text="Matricula",
                                     font="Tahoma 14 bold", fg="red")
        self.label_matricula.grid(row=0, column=0)

        # Entry
        self.txt_matricula = Entry(self.janela, font="Tahoma 14",
                                   width=27, state=DISABLED)
        self.txt_matricula.grid(row=0, column=1)

        # Label
        self.label_nome = Label(self.janela, text="Nome",
                                font="Tahoma 14 bold", fg="red")
        self.label_nome.grid(row=1, column=0)

        # Entry
        self.txt_nome = Entry(self.janela, font="Tahoma 14",
                              width=27)
        self.txt_nome.grid(row=1, column=1)

        # Label
        self.label_idade = Label(self.janela, text="Idade",
                                 font="Tahoma 14 bold", fg="red")
        self.label_idade.grid(row=2, column=0)

        # Entry
        self.txt_idade = Entry(self.janela, font="Tahoma 14",
                               width=27)
        self.txt_idade.grid(row=2, column=1)

        # Label
        self.label_curso = Label(self.janela, text="Curso",
                                 font="Tahoma 14 bold", fg="red")
        self.label_curso.grid(row=3, column=0)

        self.cursos = ['Python', 'Javascript', 'Django', 'ReactJs']
        self.cb_cursos = ttk.Combobox(self.janela, values=self.cursos, width=28,
                                      font="Tahoma 12")
        self.cb_cursos.grid(row=3, column=1)

        # Label
        self.label_nota = Label(self.janela, text="Nota",
                                font="Tahoma 14 bold", fg="red")
        self.label_nota.grid(row=4, column=0)

        # Entry
        self.txt_nota = Entry(self.janela, font="Tahoma 14",
                              width=27)
        self.txt_nota.grid(row=4, column=1)

        # botões
        self.button_adicionar = Button(self.janela, font="Tahoma 12 bold", width=7,
                                       text="Adicionar", fg="red",
                                       command=self.adicionarAluno)
        self.button_adicionar.grid(row=5, column=0)

        # botões
        self.button_editar = Button(self.janela, font="Tahoma 12 bold", width=7,
                                    text="Editar", fg="red",
                                    command=self.editarAluno)
        self.button_editar.grid(row=5, column=1)

        # botões
        self.button_deletar = Button(self.janela, font="Tahoma 12 bold", width=7,
                                     text="Deletar", fg="red",
                                     command=self.deletarAluno)
        self.button_deletar.grid(row=5, column=2)

        # frame
        self.frame = Frame(self.janela)
        self.frame.grid(row=6, column=0, columnspan=3)

        self.colunas = ['Matricula', 'Nome', 'Idade', 'Curso', 'Nota']
        self.tabela = ttk.Treeview(self.frame, columns=self.colunas, show='headings')
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
            self.tabela.column(coluna, width=110)
        self.tabela.pack()
        self.tabela.bind('<ButtonRelease-1>', self.selecionarAluno)

        self.atualizarTabela()
        self.janela.mainloop()


    def limparCampos(self):
        self.txt_nome.delete(0, END)
        self.txt_idade.delete(0, END)
        self.txt_nota.delete(0, END)
        self.cb_cursos.set("")
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.delete(0, END)
        self.txt_matricula.config(state=DISABLED)

    def atualizarTabela(self):
        # Limpa a tabela
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        alunos = self.db.select()
        for aluno in alunos:
            self.tabela.insert('', END, values=(aluno['matricula'],
                                                aluno['nome'],
                                                aluno['idade'],
                                                aluno['curso'],
                                                aluno['nota']))



    def selecionarAluno(self, event):
        linha_selecionada = self.tabela.selection()[0]
        item = self.tabela.item(linha_selecionada)['values']
        self.limparCampos()
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.insert(0, item[0])
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.insert(0, item[1])
        self.txt_idade.insert(0, str(item[2]))
        self.cb_cursos.set(item[3])
        self.txt_nota.insert(0, str(item[4]))

    def criarAluno(self):
        nome = self.txt_nome.get()
        idade = self.txt_idade.get()
        curso = self.cb_cursos.get()
        nota = float(self.txt_nota.get())
        aluno = Aluno(nome, idade, curso, nota)
        return aluno
    def adicionarAluno(self):
        aluno = self.criarAluno()
        self.db.insert(aluno)
        messagebox.showinfo('Sucesso!', 'Aluno cadastrado com sucesso!')
        self.limparCampos()
        self.atualizarTabela()

    def editarAluno(self):
        aluno = self.criarAluno()
        aluno.matricula = self.txt_matricula.get()
        self.db.update(aluno)
        messagebox.showinfo('Sucesso!', 'Aluno alterado com sucesso!')
        self.limparCampos()
        self.atualizarTabela()
    def deletarAluno(self):
        matricula = int(self.txt_matricula.get())
        self.db.delete(matricula)
        messagebox.showinfo('Sucesso!', 'Dados removido com sucesso!')
        self.limparCampos()
        self.atualizarTabela()

if __name__ == "__main__":
    app = App()