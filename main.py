# Importações ===================================================

from tkinter.ttk import *
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry 
from datetime import date
from datetime import datetime
from tkscrolledframe import ScrolledFrame
from view import *

# Cores ==========================================================

cor0 =  "#2e2d2b"  # Cinza escuro
cor1 =  "#feffff"  # Branco
cor2 =  "#4fa882"  # Verde
cor3 =  "#38576b"  # Verde 
cor4 =  "#403d3d"  # Marrom 
cor5 =  "#e06636"  # Laranja  
cor6 =  "#e9a178"  # Laranja claro
cor7 =  "#3fbfb9"  # Azul
cor8 =  "#263238"  # Verde escuro
cor9 =  "#e9edf5"  # Cinza claro
cor10 = "#6e8faf"  # Azul claro
cor11 = "#f2f4f2"  # Cinza claro
cor12 = "#dc1a1f"  # Vermelho

# Criando janela =================================================

janela = Tk()
janela.title("")
janela.geometry('780x320')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames =========================================================

frameCima = Frame(janela, width=780, height=50, bg=cor12, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265, bg=cor4, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=600, height=265, bg=cor1, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)

# Conteúdo do frameCima ==============================

# Abrindo a imagem de logo
app_imagem = Image.open('icones/logo.png')
app_imagem = app_imagem.resize((60, 40))
app_imagem = ImageTk.PhotoImage(app_imagem)

# Configuração e posicionamento da imagem de logo
app_logo = Label(frameCima, image=app_imagem, width=1000, compound=LEFT, padx=5, anchor=NW, bg=cor12, fg=cor1)
app_logo.place(x=7, y=0)

# Título principal do sistema
app_titulo = Label(frameCima, text="Sistema de Gerenciamento de Livros Alleart", compound=LEFT, padx=5, anchor=NW, font='Verdana 15 bold', bg=cor12, fg=cor1)
app_titulo.place(x=70, y=7)

# Conteúdo do frameDireita ========================

app_logo_maior = Image.open('icones/logo_maior.png')
app_logo_maior = app_logo_maior.resize((250, 150))
app_logo_maior = ImageTk.PhotoImage(app_logo_maior)
pos_logo_maior = Label(frameDireita, image=app_logo_maior, width=1000, compound=LEFT, padx=5, anchor=NW, bg=cor1, fg=cor1)
pos_logo_maior.place(x=150, y=60)

# Inserir um novo usuario =========================

def novo_usuario():

    global img_salvar

    def adicionar():
        primeiro_nome = e_p_nome.get()
        sobrenome = e_sobrenome.get()
        endereco = e_endereco.get()
        email = e_email.get()
        telefone = e_telefone.get()

        lista = [primeiro_nome, sobrenome, endereco, email, telefone]

        # Verificando caso algum campo esteja vazio ou não
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos!')
                return
        # Inserindo os dados no banco de dados
        inserir_usuario(primeiro_nome, sobrenome, endereco, email, telefone)

        # Mostrando mesnsagem de sucesso
        messagebox.showinfo('Sucesso', 'Usuário inserido com sucesso!')

        # Limpando os campos de entrada
        e_p_nome.delete(0, END)
        e_sobrenome.delete(0, END)
        e_endereco.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)
                    
    app_ = Label(frameDireita,text="Inserir um novo usuário", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)

    # Formulário de novo usuário 
    # Primeiro nome
    l_p_nome = Label(frameDireita, text="Primeiro nome*", height=1, anchor=NW, font=(' Ivy 10'), bg=cor1, fg=cor4)
    l_p_nome.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)

    e_p_nome = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_p_nome.grid(row=2, column=1, pady=10, sticky=NSEW)

    # Sobrenome
    l_sobrenome = Label(frameDireita, text="Sobrenome*",height=1, anchor=NW, font=(' Ivy 10'), bg=cor1, fg=cor4)
    l_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_sobrenome = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_sobrenome.grid(row=3, column=1, pady=5, sticky=NSEW)

    # Endereço
    l_endereco = Label(frameDireita, text="Endereço*",height=1, anchor=NW, font=(' Ivy 10 '), bg=cor1, fg=cor4)
    l_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

    e_endereco = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_endereco.grid(row=4, column=1, pady=5, sticky=NSEW)

    # E-mail
    l_email = Label(frameDireita, text="E-mail*",height=1, anchor=NW, font=(' Ivy 10 '), bg=cor1, fg=cor4)
    l_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)

    e_email = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_email.grid(row=5, column=1, pady=5, sticky=NSEW)

    # Telefone
    l_telefone = Label(frameDireita, text="Telefone*",height=1, anchor=NW, font=(' Ivy 10 '), bg=cor1, fg=cor4)
    l_telefone.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)

    e_telefone = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_telefone.grid(row=6, column=1, pady=5, sticky=NSEW)
   
    # Botao Salvar
    img_salvar = Image.open('icones/salvar.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=adicionar, image=img_salvar, compound=LEFT,width=100, text='  Salvar' ,bg=cor1, fg=cor4,font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

# Inserir um novo livro ===========================
    
def novo_livro():

    global img_salvar

    def adicionar():
        titulo = e_titulo.get()
        autor = e_autor.get()
        editora = e_editora.get()
        ano = e_ano.get()
        isbn = e_isbn.get()       

        lista = [titulo, autor, editora, ano, isbn]

        # Verificando caso algum campo esteja vazio ou não
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        # Inserindo os dados no banco de dados
        inserir_livro(titulo, autor, editora, ano, isbn)

        # Mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Livro inserido com sucesso!')

        # limpando os campos de entradas
        e_titulo.delete(0,END)
        e_autor.delete(0,END)
        e_editora.delete(0,END)
        e_ano.delete(0,END)
        e_isbn.delete(0,END)
    
    app_ = Label(frameDireita,text="Inserir um novo livro", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)

    # Formulário de novo livro 
    # Título
    l_titulo = Label(frameDireita, text="Título do livro*", height=1,anchor=NW, font=(' Ivy 10'), bg=cor1, fg=cor4)
    l_titulo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)

    e_titulo = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_titulo.grid(row=2, column=1, pady=10, sticky=NSEW)

    # Autor
    l_autor = Label(frameDireita, text="Autor do livro*",height=1,anchor=NW, font=(' Ivy 10'), bg=cor1, fg=cor4)
    l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_autor = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_autor.grid(row=3, column=1, pady=5, sticky=NSEW)

    # Editora
    l_editora = Label(frameDireita, text="Editora do livro*",height=1,anchor=NW, font=(' Ivy 10 '), bg=cor1, fg=cor4)
    l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

    e_editora = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_editora.grid(row=4, column=1, pady=5, sticky=NSEW)

    # Ano
    l_ano = Label(frameDireita, text="Ano de publicação do livro*",height=1,anchor=NW, font=(' Ivy 10 '), bg=cor1, fg=cor4)
    l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)

    e_ano = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_ano.grid(row=5, column=1, pady=5, sticky=NSEW)

    # isbn
    l_isbn = Label(frameDireita, text="ISBN do livro*",height=1,anchor=NW, font=(' Ivy 10 '), bg=cor1, fg=cor4)
    l_isbn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)

    e_isbn = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_isbn.grid(row=6, column=1, pady=5, sticky=NSEW)
   
    # Botao Salvar
    img_salvar = Image.open('icones/salvar.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=adicionar, image=img_salvar, compound=LEFT,width=100, text='  Salvar' ,bg=cor1, fg=cor4,font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

# Exibir todos os livros ============================
        
def ver_livros():

    app_ = Label(frameDireita,text="Exibir livros", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)

    dados = obter_livros()

    # Criando uma visualização em árvore com barras de rolagem duplas
    cabecalho = ['ID','Título','Autor','Editora','Ano','ISBN']
    
    global arvore

    arvore = Treeview(frameDireita, selectmode="extended",
                        columns=cabecalho, show="headings")
    
    # Barra de rolagem vertical
    vertical = Scrollbar(frameDireita, orient="vertical", command=arvore.yview)

    # Barra de rolagem horizontal
    horizontal = Scrollbar(frameDireita, orient="horizontal", command=arvore.xview)

    arvore.configure(yscrollcommand=vertical.set, xscrollcommand=horizontal.set)

    arvore.grid(column=0, row=2, sticky='nsew')
    vertical.grid(column=1, row=2, sticky='ns')
    horizontal.grid(column=0, row=3, sticky='ew')

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,165,110,100,50,50,100]
    n=0

    for coluna in cabecalho:
        arvore.heading(coluna, text=coluna, anchor='nw')
        # Ajustando a largura da coluna à string do cabeçalho
        arvore.column(coluna, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        arvore.insert('', 'end', values=item) 

# Exibir todos os usuários ========================
    
def ver_usuarios():
    
    app_ = Label(frameDireita,text="Exibir usuários", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    dados = obter_usuarios()

    # Criando uma visualização em árvore com barras de rolagem duplas
    cabecalho = ['ID', 'Nome', 'Sobrenome', 'Endereço', 'E-mail', 'Telefone']

    global arvore

    arvore = Treeview(frameDireita, selectmode="extended", columns=cabecalho, show="headings")

    # Barra de rolagem vertical
    vertical = Scrollbar(frameDireita, orient="vertical", command=arvore.yview)

     # Barra de rolagem horizontal
    horizontal = Scrollbar(frameDireita, orient="horizontal", command=arvore.xview)

    arvore.configure(yscrollcommand=vertical.set, xscrollcommand=horizontal.set)

    arvore.grid(column=0, row=2, sticky='nsew')
    vertical.grid(column=1, row=2, sticky='ns')
    horizontal.grid(column=0, row=3, sticky='ew')

    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 80, 80, 120, 120, 76, 100]
    n = 0

    for coluna in cabecalho:
        arvore.heading(coluna, text=coluna, anchor='nw')
        # Ajustando a largura da coluna à string do cabeçalho
        arvore.column(coluna, width=h[n],anchor=hd[n])

        n+=1

    for item in dados:
        arvore.insert('', 'end', values=item)
       
# Realizar um empréstimo ==========================
        
def realizar_emprestimo():

    global img_salvar

    def adicionar():
        usuario_id = e_id_usuario.get()
        livro_id = e_id_livro.get()
        data_emprestimo = e_em_data.get()
        data_devolucao = e_de_data.get()

        lista = [usuario_id, livro_id, data_emprestimo, data_devolucao]

        # Verificando caso algum campo esteja vazio ou nao
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos!')
                return

        # Inserindo os dados no banco de dados
        inserir_emprestimo(usuario_id, livro_id, data_emprestimo, data_devolucao)

        # Mostrando mesnsagem de sucesso
        messagebox.showinfo('Sucesso', 'Empréstimo realizado com sucesso!')

        # limpando os campos de entradas
        e_id_usuario.delete(0,END)
        e_id_livro.delete(0,END)
        e_em_data.delete(0,END)
        e_de_data.delete(0,END)

    app_ = Label(frameDireita,text="Realizar um empréstimo", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
 
    # Formulário de realizar empréstimo
    # ID do usuário
    l_id = Label(frameDireita, text="Digite o ID do usuário*", height=1, anchor=NW, font=(' Ivy 10'), bg=cor1, fg=cor4)
    l_id.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)

    e_id_usuario = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_id_usuario.grid(row=2, column=1, pady=10, sticky=NSEW)

    # ID do livro
    l_id = Label(frameDireita, text="Digite o ID do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=cor1, fg=cor4)
    l_id.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)

    e_id_livro = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_id_livro.grid(row=3, column=1, pady=5, sticky=NSEW)

    # Data do empréstimo
    em_id = Label(frameDireita, text="Digite a data do empréstimo (formato: AAAA-MM-DD)*",height=1, anchor=NW, font=(' Ivy 10'), bg=cor1, fg=cor4)
    em_id.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)

    e_em_data = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_em_data.grid(row=4, column=1, pady=5, sticky=NSEW)

    # Data da devolução
    de_id = Label(frameDireita, text="Digite a data da devolução (formato: AAAA-MM-DD)*",height=1, anchor=NW, font=(' Ivy 10'), bg=cor1, fg=cor4)
    de_id.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)

    e_de_data = Entry(frameDireita, width=25, justify='left',relief="solid")
    e_de_data.grid(row=5, column=1, pady=5, sticky=NSEW)

    # Botao Salvar
    img_salvar = Image.open('icones/salvar.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=adicionar, image=img_salvar, compound=LEFT,width=100, text='  Salvar' ,bg=cor1, fg=cor4, font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

# Livros emprestados no momento ===================
    
def ver_livros_emprestados():

    app_ = Label(frameDireita,text="Livros emprestados", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)

    dados = livros_emprestados()
   
   # Criando uma visualização em árvore com barras de rolagem duplas
    cabecalho = ['ID Empréstimo','ID do usuário','ID do livro','Data empréstimo','Data devolução']     
   
    global arvore

    arvore = Treeview(frameDireita, selectmode="extended",
                        columns=cabecalho, show="headings")
    
    # Barra de rolagem vertical
    vertical  = Scrollbar(frameDireita, orient="vertical", command=arvore.yview)

    # Barra de rolagem horizontal
    horizontal = Scrollbar(frameDireita, orient="horizontal", command=arvore.xview)

    arvore.configure(yscrollcommand=vertical.set, xscrollcommand=horizontal.set)

    arvore.grid(column=0, row=2, sticky='nsew')
    vertical.grid(column=1, row=2, sticky='ns')
    horizontal.grid(column=0, row=3, sticky='ew')
    
    hd=["nw","nw","ne","ne","ne","ne"]
    h=[20,175,120,90,90,100,100]
    n=0

    for coluna in cabecalho:
        arvore.heading(coluna, text=coluna, anchor='nw')
        # Ajustando a largura da coluna à string do cabeçalho
        arvore.column(coluna, width=h[n], anchor=hd[n])
        
        n+=1

    for item in dados:
        arvore.insert('', 'end', values=item) 
 
# Função para controlar o Menu ==================================== 
        
def control(i):
    # Novo usuário
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # Chamando a função novo_usuario
        novo_usuario()

    # Novo livro
    if i == 'novo_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        novo_livro()

    # Ver livros
    if i == 'ver_livros':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_livros()

    # Ver usuários
    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # Chamando a função ver_usuarios
        ver_usuarios()

    # Realizar um empréstimo
    if i == 'realizar_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        realizar_emprestimo()

    # Livros emprestados no momento
    if i == 'ver_livros_emprestados':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_livros_emprestados()

# Menu ========================================= 

# Novo usuario
img_usuario = Image.open('icones/adicionar.png')
img_usuario = img_usuario.resize((18, 18))
img_usuario = ImageTk.PhotoImage(img_usuario)
b_usuario = Button(frameEsquerda, command=lambda:control('novo_usuario'), image=img_usuario, compound=LEFT, anchor=NW, text='Novo usuário', bg=cor4, fg=cor1, font=('Ivy 11'))
b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# Novo livro
img_novo_livro = Image.open('icones/adicionar.png')
img_novo_livro = img_novo_livro.resize((18, 18))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
b_novo_livro = Button(frameEsquerda, command=lambda:control('novo_livro'), image=img_novo_livro, compound=LEFT, anchor=NW, text='Novo livro', bg=cor4, fg=cor1, font=('Ivy 11'))
b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Exibir todos os livros
img_ver_livro = Image.open('icones/logo.png')
img_ver_livro = img_ver_livro.resize((18, 18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
b_ver_livro = Button(frameEsquerda, command=lambda:control('ver_livros'), image=img_ver_livro, compound=LEFT, anchor=NW, text='Exibir todos os livros', bg=cor4, fg=cor1, font=('Ivy 11'))
b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# Exibir todos os usuários
img_ver_usuario = Image.open('icones/usuario.png')
img_ver_usuario = img_ver_usuario.resize((18, 18))
img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)
b_ver_usuario = Button(frameEsquerda, command=lambda:control('ver_usuarios'), image=img_ver_usuario, compound=LEFT, anchor=NW, text='Exibir todos os usuários', bg=cor4, fg=cor1, font=('Ivy 11'))
b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

# Realizar um empréstimo
img_emprestimo = Image.open('icones/adicionar.png')
img_emprestimo = img_emprestimo.resize((18, 18))
img_emprestimo = ImageTk.PhotoImage(img_emprestimo)
b_emprestimo = Button(frameEsquerda, command=lambda:control('realizar_emprestimo'), image=img_emprestimo, compound=LEFT, anchor=NW, text='Realizar um empréstimo', bg=cor4, fg=cor1, font=('Ivy 11'))
b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Livros emprestados no momento
img_livros_emprestados = Image.open('icones/livro2.png')
img_livros_emprestados = img_livros_emprestados.resize((18, 18))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
b_livros_emprestados = Button(frameEsquerda, command=lambda:control('ver_livros_emprestados'), image=img_livros_emprestados, compound=LEFT, anchor=NW, text='Livros emprestados no momento', bg=cor4, fg=cor1, font=('Ivy 11'))
b_livros_emprestados.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

l_creditos = Label(frameEsquerda, compound=LEFT, anchor=NW, text='SGL Alleart | Todos os direitos reservados | © 2024', bg=cor4, fg=cor1, font=('Ivy 8'))
l_creditos.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

janela.mainloop()