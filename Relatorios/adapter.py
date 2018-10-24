import abc
import pandas as pd


class Target(metaclass=abc.ABCMeta):
    """
    Defina a interface específica do domínio que o Cliente usa.
    """
    def __init__(self, data):
        self.data = RelatorioCSV(data)

    @abc.abstractmethod
    def request(self, arg):
        pass

class Adapter(Target):
    """
    Adapte a interface do Adaptee à interface do Target.
    """
    def request(self, arg):
        if arg == 1: self.data.gerar_csv()
        elif arg == 2: self.txt()

    def txt(self):
        with open('relatorio.txt', 'w') as file:
            for _ in range(len(self.data.data)):
                file.write(str(self.data.data.iloc[_]))
                file.write("\n")
                file.write("---------------------------------------"
                           "---------------------------------------")
                file.write("\n")

class RelatorioCSV:
    """
    Define uma interface existente que precisa ser adaptada.
    """
    def __init__(self, data):
        self.data = data

    def gerar_csv(self):
        df = pd.DataFrame(self.data)
        df.to_csv('relatorio.csv', ';')

def main(data, arg):
    data = data
    adapter = Adapter(data)
    adapter.request(arg)