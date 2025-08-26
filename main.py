from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color


class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 25
        self.spacing = 20

        # Fundo colorido
        with self.canvas.before:
            Color(0.05, 0.05, 0.1, 1)  # azul escuro quase preto
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        # Título
        self.label_titulo = Label(
            text="🔮 Verificador de Idade 🔮",
            font_size=32,
            color=(0.2, 0.8, 1, 1),  # azul neon
            bold=True
        )
        self.add_widget(self.label_titulo)

        # Campo nome
        self.nome_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            font_size=20,
            background_color=(0.15, 0.15, 0.25, 1),
            foreground_color=(0.9, 0.9, 1, 1),
            cursor_color=(0.2, 0.8, 1, 1),
            size_hint_y=None,
            height=50
        )
        self.add_widget(self.nome_input)

        # Campo idade
        self.idade_input = TextInput(
            hint_text="Digite sua idade",
            multiline=False,
            font_size=20,
            background_color=(0.15, 0.15, 0.25, 1),
            foreground_color=(0.9, 0.9, 1, 1),
            cursor_color=(0.2, 0.8, 1, 1),
            size_hint_y=None,
            height=50
        )
        self.add_widget(self.idade_input)

        # Botão enviar
        self.botao = Button(
            text="🚀 Enviar",
            font_size=24,
            size_hint_y=None,
            height=65,
            background_normal="",  # necessário p/ aplicar a cor
            background_color=(0, 1, 0.5, 1)  # verde neon
        )
        self.botao.bind(on_release=self.verificar_idade)
        self.add_widget(self.botao)

        # Label resposta
        self.label_resposta = Label(
            text="",
            font_size=22,
            color=(1, 0.6, 0.2, 1),  # laranja neon
            halign="center",
            valign="middle"
        )
        self.label_resposta.bind(size=self._update_text_size)
        self.add_widget(self.label_resposta)

    def _update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def _update_text_size(self, instance, value):
        """Centraliza texto corretamente"""
        instance.text_size = instance.size

    def verificar_idade(self, instance):
        nome = self.nome_input.text.strip()
        idade_texto = self.idade_input.text.strip()

        mensagem = "⚠️ Por favor, preencha os campos corretamente."
        cor = (1, 0.2, 0.2, 1)  # vermelho neon

        if nome and idade_texto:
            try:
                idade = int(idade_texto)
                if idade < 0:
                    mensagem = f"❌ Idade inválida, {nome}!"
                    cor = (1, 0.5, 0, 1)  # laranja neon
                elif idade < 18:
                    mensagem = f"👶 Olá, {nome}! Você é menor de idade."
                    cor = (0.8, 0.5, 1, 1)  # roxo neon
                elif idade >= 60:
                    mensagem = f"🧓 Olá, {nome}! Você é idoso e merece muito respeito ❤️."
                    cor = (1, 0.8, 0.2, 1)  # dourado neon
                else:
                    mensagem = f"🧑 Olá, {nome}! Você é maior de idade."
                    cor = (0.2, 1, 0.6, 1)  # verde neon
            except ValueError:
                mensagem = "⚠️ Digite um número válido para idade."
                cor = (1, 0.2, 0.2, 1)

        # aplica de uma vez
        self.label_resposta.text = mensagem
        self.label_resposta.color = cor


class IdadeApp(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    IdadeApp().run()
