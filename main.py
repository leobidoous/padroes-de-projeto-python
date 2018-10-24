from kivy.uix.boxlayout import BoxLayout

from Controller import controller as ctlr

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import kivy
from kivy.uix.popup import Popup

kivy.require('1.10.0')

#     MANIPULAÇÃO DA FÁBRICA
#
#     self._factory[1][2][3][4][5][6]
#
# [1]
#     se 0: Nome da universidade selecionada
#     se 1: Acesso aos departamentos da universidade selecionada
# [2]
#     se 0: Seleciona o primeiro departamento
#     se 1: Seleciona o segundo departamento
#     se n: Seleciona o enésimo departamento
# [3]
#     se 0: Acesso ao nome do departamento selecionado
#     se 1: Acesso aos cursos e disciplinas do departamento
# [4]
#     se 0: Seleciona o primeiro curso
#     se 1: Seleciona o segundo curso
#     se n: Seleciona o enésimo curso
# [5]
#     se 0: Seleciona o nome do curso
#     se 1: Acesso às disciplinas do curso
# [6]
#     se 0: Seleciona a primeira disciplina
#     se 1: Seleciona a segunda disciplina
#     se n: Seleciona a enésima disciplina

# #################################################### INTERFACE GRÁFICA
class TelaPrincipal(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._factory = ctlr.choose_factory(None)

        self._disciplinas_aluno = []
        self._alunos = []

        self.ids.type_uni.bind(text=self.choosebox_1)
        self.ids.type_depart.bind(text=self.choosebox_2)
        self.ids.type_curso.bind(text=self.choosebox_3)
        self.ids.type_disc.bind(text=self.choosebox_4)

    # ChooseBox para escolha da universidade
    def choosebox_1(self, text, arg0):
        self._departamentos = []
        self.ids.type_depart.values = []
        self.ids.type_depart.text = "Departamentos[color=ff3333] *[/color]"
        self.ids.type_curso.values = []
        self.ids.type_curso.text = "Cursos[color=ff3333] *[/color]"
        self.ids.type_disc.values = []
        self.ids.type_disc.text = "Disciplinas"
        self._disciplinas_aluno = []
        try:
            self._factory = ctlr.choose_factory(arg0)
            for _ in range(len(self._factory[1])):
                self._departamentos.append(self._factory[1][_][0])
            self.ids.type_depart.values = self._departamentos
        except:
            return None

    # ChooseBox para escolha do departamento
    def choosebox_2(self, text, arg0):
        self._cursos = []
        self.ids.type_curso.values = []
        self.ids.type_curso.text = "Cursos[color=ff3333] *[/color]"
        self.ids.type_disc.values = []
        self.ids.type_disc.text = "Disciplinas"
        self._disciplinas_aluno = []
        for _ in range(len(self._factory[1])):
            if arg0 == self._factory[1][_][0]:
                for i in range(len(self._factory[1][_][1])):
                    self._cursos.append(self._factory[1][_][1][i][0])
        self.ids.type_curso.values = self._cursos

    # ChooseBox para escolha do curso
    def choosebox_3(self, text, arg0):
        self._disciplinas = []
        self.ids.type_disc.values = []
        self.ids.type_disc.text = "Disciplinas"
        self._disciplinas_aluno = []
        for _ in range(len(self._factory[1])):
            if str(self.ids.type_depart.text) == self._factory[1][_][0]:
                for i in range(len(self._factory[1][_][1])):
                    if arg0 == self._factory[1][_][1][i][0]:
                        for j in range(len(self._factory[1][_][1][i][1])):
                            self._disciplinas.append(self._factory[1][_][1][i][1][j])
        self.ids.type_disc.values = self._disciplinas

    # ChooseBox para escolha das disciplinas
    def choosebox_4(self, text, arg0):
        if arg0 in self.ids.type_disc.values:
            self._disciplinas_aluno.append(arg0)
            self.ids.type_disc.values.remove(arg0)
            if len(self.ids.type_disc.values) == 0:
                self.ids.type_disc.text = "Sem disciplinas para adicionar"

    # Exibe poup-up de confirmação de cadastro de aluno
    def confirmacao(self):
        content = Button(text='Aluno inserido')
        popup = Popup(title='Inserir Aluno', content=content, size_hint=(None, None),
                      size=(250, 100), auto_dismiss=False)

        content.bind(on_press=popup.dismiss)
        popup.open()

    # Exibe poup-up de campo vazio nos inputs do formulário de cadastro
    def _campo_vazio(self):
        content = Button(text='Preencha todos os campos.')
        popup = Popup(title='Campos vazios', content=content,size_hint=(None, None),
                      size=(250, 100), auto_dismiss=False)
        content.bind(on_press=popup.dismiss)
        popup.open()

    # Verifica se os campos estão preenchidos e adiciona o aluno
    def add_aluno(self):
        if self.ids.type_uni.text == "Universidades[color=ff3333] *[/color]": return self._campo_vazio()
        elif self.ids.type_depart.text == "Departamentos[color=ff3333] *[/color]": return self._campo_vazio()
        elif self.ids.type_curso.text == "Cursos[color=ff3333] *[/color]": return self._campo_vazio()
        elif self.ids.nome.text == '': return self._campo_vazio()
        elif self.ids.cpf.text == '': return self._campo_vazio()
        elif self.ids.matricula.text == '': return self._campo_vazio()
        else:
            self._alunos.append(ctlr.create_student(self.ids.nome.text, self.ids.cpf.text,
                                                    self.ids.matricula.text, self.ids.type_uni.text,
                                                    self.ids.type_depart.text, self.ids.type_curso.text,
                                                    self._disciplinas_aluno))

            self.ids.type_uni.text = "Universidades[color=ff3333] *[/color]"
            self.ids.type_depart.text = "Departamentos[color=ff3333] *[/color]"
            self.ids.type_curso.text = "Cursos[color=ff3333] *[/color]"
            self.ids.nome.text = ''
            self.ids.cpf.text = ''
            self.ids.matricula.text = ''
            self._disciplinas_aluno = []
            self.ids.type_disc.text = "Disciplinas"
            self.ids.view.text = ''

            self.confirmacao()

    # Lista os alunos já cadastrados caso haja
    def listar(self):
        _aux1 = ctlr.create_iterator(self._alunos)
        if not _aux1 == []:
            _aux2 = ctlr.create_sort(_aux1)
            self.ids.view.text = ''
            for i in range(len(_aux2)):
                self.ids.view.text += str(_aux2.iloc[i])
                self.ids.view.text += '\n--------------------------------' \
                                      '----------------------------------' \
                                      '----------------------------------' \
                                      '--------------------------------\n'
        else:
            self.ids.view.text = ''
            self.ids.view.text += 'NENHUM ALUNO CADASTRADO.'

    # Gera relatório contendo os dados dos alunos cadastrados caso haja
    def gerar_relatorio(self):
        _aux1 = ctlr.create_iterator(self._alunos)
        def report_created():
            box = BoxLayout(orientation='horizontal', padding=5, spacing=5)
            btn_ok = Button(text="Relatório gerado")
            box.add_widget(btn_ok)
            popup = Popup(title='Exportar relatório',
                          content=box,
                          size_hint=(None, None), size=(250, 100),
                          auto_dismiss=False)
            btn_ok.bind(on_press=popup.dismiss)
            popup.open()

        def csv(self):
            _aux2 = ctlr.create_sort(_aux1)
            ctlr.create_report(_aux2, 1)
            report_created()
        def txt(self):
            _aux2 = ctlr.create_sort(_aux1)
            ctlr.create_report(_aux2, 2)
            report_created()
        if not _aux1 == []:

            box = BoxLayout(orientation='vertical', padding=5, spacing=5)
            btn_csv = Button(text="CSV")
            btn_txt = Button(text="TXT")
            btn_back = Button(text="Voltar")
            box.add_widget(btn_csv)
            box.add_widget(btn_txt)
            box.add_widget(btn_back)
            popup = Popup(title='Exportar relatório',
                          content=box,
                          size_hint=(None, None), size=(250, 200),
                          auto_dismiss=True)
            btn_csv.bind(on_press=csv)
            btn_txt.bind(on_press=txt)
            btn_back.bind(on_press=popup.dismiss)
            popup.open()
        else:
            box = BoxLayout(orientation='horizontal', padding=5, spacing=5)
            btn = Button(text='Nenhum dado encontrado')
            box.add_widget(btn)
            popup = Popup(title='Gerar Relatório',
                          content=box,
                          size_hint=(None, None), size=(250, 100),
                          auto_dismiss=False)
            btn.bind(on_press=popup.dismiss)
            popup.open()

# Cria e executa a interface
class Interface(App):
    def build(self):
        self.title = "UniDESK Gestor LTDA."
        return TelaPrincipal()

run = Interface()
run.run()