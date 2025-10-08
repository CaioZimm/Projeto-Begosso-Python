class Curso:
    def __init__(self, codigocurso, nomecurso):
        self.codigocurso = codigocurso
        self.nomecurso = nomecurso

    def __str__(self):
        return f"{self.codigocurso} - {self.nomecurso}"

    def __lt__(self, other):
        return self.codigocurso < other.codigocurso
