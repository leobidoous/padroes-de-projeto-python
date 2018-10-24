import abc

#CLASSE ABSTRADA DE CURSOS QUE COMPÕEM UMA DISCIPLINA
class Disciplinas(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def nome(self):
        pass

class Filosofia(Disciplinas):
    def __init__(self):
        self._nome = "FIT4252 - Filosofia"

    def nome(self):
        return self._nome

class Calculo(Disciplinas):
    def __init__(self):
        self._nome = "MAF2701 - Cálculo I"

    def nome(self):
        return self._nome

class Fisica(Disciplinas):
    def __init__(self):
        self._nome = "MAF1201 - Eletricidade e Eletrônica"

    def nome(self):
        return self._nome

class Anatomia(Disciplinas):
    def __init__(self):
        self._nome = "MED1025 - Anatomia III"

    def nome(self):
        return self._nome

class Portugues(Disciplinas):
    def __init__(self):
        self._nome = "LET2354 - Português I"

    def nome(self):
        return self._nome

class Topografia(Disciplinas):
    def __init__(self):
        self._nome = "ENG1204 - Topografia II"

    def nome(self):
        return self._nome