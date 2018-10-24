import abc
from Disciplinas import disciplinas as disc

#CLASSE ABSTRADA DE CURSOS QUE COMPÕEM UMA CURSOS
class Cursos(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def metodo_abstrato(self):
        pass

#CLASSES QUE DERIVAM DE CURSOS
class Direito(Cursos):
    def __init__(self):
        self._nome = "Direito"

    def metodo_abstrato(self):
        return self._nome, disc.DiscHumanas().metodo_abstrato()

class Arquitetura(Cursos):
    def __init__(self):
        self._nome = "Arquitetura"

    def metodo_abstrato(self):
        return self._nome, disc.DiscExatas().metodo_abstrato()

class Computacao(Cursos):
    def __init__(self):
        self._nome = "Computação"

    def metodo_abstrato(self):
        return self._nome, disc.DiscExatas().metodo_abstrato()

class Administracao(Cursos):
    def __init__(self):
        self._nome = "Administração"

    def metodo_abstrato(self):
        return self._nome, disc.DiscExatas().metodo_abstrato()

class Biologia(Cursos):
    def __init__(self):
        self._nome = "Biologia"

    def metodo_abstrato(self):
        return self._nome, disc.DiscBiologicas().metodo_abstrato()