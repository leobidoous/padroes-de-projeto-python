class Alunos:
    def __init__(self):
        self._nome = None
        self._cpf = None
        self._matricula = None
        self._universidade = None
        self._departamento_vinculado = None
        self._curso = None
        self._disciplinas = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @property
    def universidade(self):
        return self._universidade

    @universidade.setter
    def universidade(self, universidade):
        self._universidade = universidade

    @property
    def departamento_vinculado(self):
        return self._departamento_vinculado

    @departamento_vinculado.setter
    def departamento_vinculado(self, departamento_vinculado):
        self._departamento_vinculado = departamento_vinculado

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        self._curso = curso

    @property
    def disciplinas(self):
        return self._disciplinas

    @disciplinas.setter
    def disciplinas(self, disciplinas):
        self._disciplinas = disciplinas

