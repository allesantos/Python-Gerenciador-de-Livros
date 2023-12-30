import sqlite3

# Função para conectar ao banco de dados ==============================
def connect():
    conexao = sqlite3.connect('dados.db')
    return conexao

# Função para inserir um novo livro na tabela "livros" ==============================
def inserir_livro(titulo, autor, editora, ano_publicacao, isbn):
    conexao = connect()
    conexao.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn)\
                     VALUES(?, ?, ?, ?, ?)",(titulo, autor, editora, ano_publicacao, isbn))
    conexao.commit()
    conexao.close()

# Função que retorna todos os livros do banco de dados ==============================
def obter_livros():
    conexao = connect()
    c = conexao.cursor()
    c.execute("SELECT * FROM livros")
    books = c.fetchall()
    conexao.close()
    return books
    
# Função para inserir um novo usuário na tabela "usuarios" ==============================
def inserir_usuario(nome, sobrenome, endereco, email, telefone):
    conexao = connect()
    conexao.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone)\
                     VALUES(?, ?, ?, ?, ?)",(nome, sobrenome, endereco, email, telefone))
    conexao.commit()
    conexao.close()

# Função que retorna todos os usuários do banco de dados ==============================
def obter_usuarios():
    conexao = connect()
    c = conexao.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    conexao.close()
    return users

# Função para inserir um novo empréstimo na tabela "emprestimos" ===============
def inserir_emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conexao = connect()
    conexao.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                    VALUES(?, ?, ?, ?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conexao.commit()
    conexao.close()

# Função para recuperar todos os livros emprestados no momento ==============================
def livros_emprestados():
    conexao = connect()
    c = conexao.cursor()
    c.execute("SELECT emprestimos.id, emprestimos.id_livro, emprestimos.id_usuario, emprestimos.data_emprestimo, emprestimos.data_devolucao FROM emprestimos")
    books = c.fetchall()
    conexao.close()
    return books

# Função para atualizar a data de devolução de um empréstimo ==============================
def update_data_devolucao(id_emprestimo, data_devolucao):
    conexao = connect()
    conexao.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
    conexao.commit()
    conexao.close()
