from Universidades import universidades as factory
from Alunos import alunos as student
from TemplateMethod import template_method as tmp
from Relatorios import adapter as adpt
from Iterator import iterator as iter

# Cria a instância da FÁBRICA de universidades utilizando SINGLETON
def choose_factory(arg0):
    if arg0 == 'PUC': return factory.PUC().metodo_abstrato()
    elif arg0 == 'UFG': return factory.UFG().metodo_abstrato()
    else: return None

# Cria o aluno
def create_student(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    obj_student = student.Alunos()

    obj_student.nome = arg0
    obj_student.cpf = arg1
    obj_student.matricula = arg2
    obj_student.universidade = arg3
    obj_student.departamento_vinculado = arg4
    obj_student.curso = arg5
    obj_student.disciplinas = arg6

    return obj_student

# Cria o ITERATOR
def create_iterator(arg0):
    iterator = iter.main(arg0)
    return iterator

# Ordena utilizando o TEMPLATE
def create_sort(arg0):
    ordered = tmp.main(arg0)
    return ordered

# Gera o relatório utilizando o ADAPTER
def create_report(arg0, arg1):
    if arg1 == 1: adpt.main(arg0, arg1)
    elif arg1 == 2: adpt.main(arg0, arg1)
    else: return None