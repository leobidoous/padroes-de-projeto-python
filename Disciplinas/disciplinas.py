import abc
from Disciplinas import lista_disciplinas as l_disc
#CLASSE ABSTRADA DE CURSOS QUE COMPÕEM UMA DISCIPLINA
class ConjDisciplinas(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def metodo_abstrato(self):
        pass

#CLASSES QUE DERIVAM DE DISCIPLINA
class DiscExatas(ConjDisciplinas):
    def metodo_abstrato(self):
        return [l_disc.Fisica().nome(), l_disc.Topografia().nome(),
                l_disc.Calculo().nome(), l_disc.Portugues().nome(),
                l_disc.Filosofia().nome()]

class DiscHumanas(ConjDisciplinas):
    def metodo_abstrato(self):
        return [l_disc.Portugues().nome(), l_disc.Filosofia().nome()]

class DiscBiologicas(ConjDisciplinas):
    def metodo_abstrato(self):
        return [l_disc.Anatomia().nome(), l_disc.Portugues().nome(),
                l_disc.Filosofia().nome()]