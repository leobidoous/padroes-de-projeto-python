import abc
import pandas as pd

class TemplateMethod(metaclass=abc.ABCMeta):
    def __init__(self, iterator):
        self.iterator = pd.DataFrame(data=iterator)

    @abc.abstractmethod
    def Ordenar(self):
        pass

class TemplateOrdenar(TemplateMethod):
    def Ordenar(self):
        return self.iterator.sort_values([0, 1, 2, 5], ascending=True)

def main(arg0):
    return TemplateOrdenar(arg0).Ordenar()