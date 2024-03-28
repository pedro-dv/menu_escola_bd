import pymysql
from aluno import Aluno


class AlunoBanco:
    def __init__(self, host: str, username: str, db: str, password: str):
        self.conexao = self.criarConexao(host, username, db, password)
        self.cursor = self.conexao.cursor()

    def criarConexao(self, host: str, username: str, db: str, password: str):
        try:
            conn = pymysql.connect(host=host, user=username, db=db, password=password,
                                   cursorclass=pymysql.cursors.DictCursor)
            return conn
        except Exception as erro:
            print(f"Erro ao conectar ao banco! Erro: {erro}")

    def insert(self, aluno: Aluno):
        try:
            sql = ("insert into alunos (matricula, nome, idade, curso, nota)"
                   "values (%s, %s, %s, %s, %s)")
            self.cursor.execute(sql, (aluno.matricula, aluno.nome,
                                      aluno.idade, aluno.curso, aluno.nota))
            self.conexao.commit()
            print('Aluno cadastrado com sucesso!')
        except Exception as erro:
            print(f"Erro ao inserir! Erro: {erro}")

    def update(self, aluno: Aluno):
        try:
            sql = ("update alunos set nome = %s, idade = %s, curso = %s, nota = %s "
                   "where matricula = %s")
            self.cursor.execute(sql, (aluno.nome,
                                      aluno.idade, aluno.curso, aluno.nota, aluno.matricula))
            self.conexao.commit()
            print('Aluno editado com sucesso!')
        except Exception as erro:
            print(f"Erro ao Editar! Erro: {erro}")

    def delete(self, matricula: int):
        try:
            sql = ("delete from alunos where matricula = %s")

            self.cursor.execute(sql, matricula)
            self.conexao.commit()
            print('Aluno deletado com sucesso!')
        except Exception as erro:
            print(f"Erro ao deletar! Erro: {erro}")

    def select(self):
        try:
            sql = "select * from alunos"
            self.cursor.execute(sql)
            alunos = self.cursor.fetchall()
            return alunos
        except Exception as erro:
            print(f"Erro ao listar! Erro: {erro}")


if __name__ == '__main__':
    a = AlunoBanco('localhost', 'root', 'escola', '')

    aluno1 = Aluno('pedro', 29, 'python', 9)
    aluno2 = Aluno('ph', 19, 'python', 7)

    a.insert(aluno1)
    a.insert(aluno2)
    print(a.select())
    aluno1.nome = 'Pedro henrique'
    a.update(aluno1)
    print(a.select())
    a.delete(aluno2.matricula)
    print(a.select())
