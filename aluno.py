import uuid
class Aluno:
    matricula = 0
    def __init__(self, nome: str, idade: int, curso: str, nota: float):
        Aluno.matricula += 1
        self.matricula = uuid.uuid4()
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

    def __repr__(self):
        return (f"({self.matricula}, {self.nome}, {self.idade}, "
                f"{self.curso}, {self.nota})")

if __name__ == "__main__":
    print(Aluno('pedro', 29, 'python', 10))