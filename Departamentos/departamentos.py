import abc
from Cursos import cursos

#CLASSE ABSTRADA DE CURSOS QUE COMPÕEM UMA DEPARTAMENTOS
class Departamentos(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def metodo_abstrato(self):
        pass

class Exatas(Departamentos):
    _nome_departamento = "Exatas"
    def metodo_abstrato(self):
        return self._nome_departamento, [cursos.Computacao().metodo_abstrato(),
                                         cursos.Arquitetura().metodo_abstrato()]

class Biologicas(Departamentos):
    _nome_departamento = "Biológicas"
    def metodo_abstrato(self):
        return self._nome_departamento, [cursos.Biologia().metodo_abstrato()]

class Humanas(Departamentos):
    _nome_departamento = "Humanas"
    def metodo_abstrato(self):
        return self._nome_departamento, [cursos.Direito().metodo_abstrato()]