from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class ListaTarefas(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 15

        # Título
        self.add_widget(Label(
            text="📝 Minha Lista de Tarefas",
            font_size="24sp",
            size_hint_y=None,
            height=50,
            bold=True
        ))

        # Entrada de texto
        self.entrada = TextInput(
            hint_text="Digite uma tarefa...",
            multiline=False,
            size_hint_y=None,
            height=40
        )
        self.add_widget(self.entrada)

        # Botão Adicionar
        btn_add = Button(
            text="Adicionar",
            size_hint_y=None,
            height=40,
            background_color=(0.2, 0.7, 0.2, 1)
        )
        btn_add.bind(on_release=lambda x: self.adicionar_tarefa())
        self.add_widget(btn_add)

        # Botão Limpar lista
        btn_clear = Button(
            text="Limpar lista",
            size_hint_y=None,
            height=40,
            background_color=(0.8, 0.2, 0.2, 1)
        )
        btn_clear.bind(on_release=lambda x: self.limpar_lista())
        self.add_widget(btn_clear)

        # Mensagem de erro/aviso
        self.mensagem = Label(
            text="",
            color=(1, 0, 0, 1),
            size_hint_y=None,
            height=30
        )
        self.add_widget(self.mensagem)

        # Área de tarefas (com ScrollView)
        self.scroll = ScrollView()
        self.lista = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            spacing=5
        )
        self.lista.bind(minimum_height=self.lista.setter("height"))
        self.scroll.add_widget(self.lista)
        self.add_widget(self.scroll)

    def adicionar_tarefa(self):
        texto = self.entrada.text.strip()

        if texto:
            nova_tarefa = Label(
                text=f"• {texto}",
                size_hint_y=None,
                height=30
            )
            self.lista.add_widget(nova_tarefa)
            self.entrada.text = ""
            self.mensagem.text = ""
        else:
            self.mensagem.text = "⚠ Insira uma tarefa válida"

    def limpar_lista(self):
        self.lista.clear_widgets()
        self.mensagem.text = "Lista limpa!"


class TarefasApp(App):
    def build(self):
        return ListaTarefas()


if __name__ == '__main__':
    TarefasApp().run()
