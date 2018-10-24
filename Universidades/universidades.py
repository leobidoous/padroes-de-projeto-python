import abc
from random import randint, seed
from Departamentos import departamentos as depart

#FÁBRICA DE UNIVERSIDADES
class Universidades(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def metodo_abstrato(self):
        pass

#OBJETOS DERIVADOS DA FÁBRICA UNIVERSIDADES
class PUC(Universidades):
    def __init__(self):
        self._nome = "PUC"

    _instancia = None
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            seed(1)
            cls._codigo_universidade = randint(1, 10001)
            cls._instancia = super(PUC, cls).__new__(cls)
        return cls._instancia

    def metodo_abstrato(self):
        return [self._nome, self._codigo_universidade], [depart.Exatas().metodo_abstrato(),
                                                         depart.Humanas().metodo_abstrato(),
                                                         depart.Biologicas().metodo_abstrato()]

class UFG(Universidades):
    def __init__(self):
        self._nome = "UFG"

    _instancia = None
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            seed(2)
            cls._codigo_universidade = randint(0, 1001)
            cls._instancia = super(UFG, cls).__new__(cls)
        return cls._instancia

    def metodo_abstrato(self):
        return [self._nome, self._codigo_universidade], [depart.Humanas().metodo_abstrato(),
                                                         depart.Biologicas().metodo_abstrato()]