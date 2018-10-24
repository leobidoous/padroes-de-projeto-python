class Iterable:
    # CONSTRUTOR DO ITERABLE
    def __init__(self, iterator):
        self.iterator = iterator

    def __iter__(self):
        return Iteration(self.iterator)

class Iteration:
    # CONSTRUTOR DO ITERATION
    def __init__(self, iterator):
        self.index = 0
        self.iterator = iterator

    def __next__(self):
        # CONDIÇÃO PARA RETORNAR OS INDICES
        if self.index < len(self.iterator):
            object = []
            object.append(self.iterator[self.index].universidade)
            object.append(self.iterator[self.index].departamento_vinculado)
            object.append(self.iterator[self.index].curso)
            object.append(self.iterator[self.index].matricula)
            object.append(self.iterator[self.index].cpf)
            object.append(self.iterator[self.index].nome)
            for j in range(len(self.iterator[self.index].disciplinas)):
                object.append(self.iterator[self.index].disciplinas[j])
            self.index = self.index + 1
            return object
        # FUNÇÃO DE SISTEMA QUE VERIFICA SE ACABARAM OS INDICES DE RETORNO
        else:
            raise StopIteration()

def main(arg0):

    Iterator = Iterable(arg0)
    FirstIterator = iter(Iterator)
    list_iterable = []
    while True:
        try:
            list_iterable.append(next(FirstIterator))
        except StopIteration:
            return list_iterable