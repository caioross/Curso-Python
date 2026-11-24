import sqlite3

# Conectar ao banco de dados ( ou criar um novo se nao existir)

def conectarBanco() :
    conexao = sqlite3.connect('exemplo.db')
    return conexao

# Vamos criar uma tabela
def criarTabela() :
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        idade INTEGER
                   )
                   ''')
    conexao.commit()
    conexao.close()
    
def inserirUsuario(nome, idade) :
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
                   INSERT INTO usuarios (nome,idade) VALUES (?, ?)
                   ''', (nome, idade))
    conexao.commit()
    conexao.close()
    
def listarUsuarios() :
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios :
        print(usuario)
    conexao.close()

# Atualizar usuarios
def atualizarUsuario(id, novoNome, novaIdade):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?', (novoNome, novaIdade, id))
    conexao.commit()
    conexao.close()
    
def excluirUsuario(id) :
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute(' DELETE FROM usuarios WHERE id = ? ', (id,))
    conexao.commit()
    conexao.close()

# Executar a criação do banco
criarTabela()

# Vamos inserir um usuario
inserirUsuario("Caio",39)
inserirUsuario("Lucas", 25)
inserirUsuario("Rafael", 20)
inserirUsuario("Leonardo", 35)
inserirUsuario("Nicole", 16)

# Ver dados armazenados
listarUsuarios()

# Editar um usuario
atualizarUsuario(1, "Henrique", 66)

# Excluir Usuario
excluirUsuario(4)