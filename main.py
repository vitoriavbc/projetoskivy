import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class FilmeApp(App):
    def build(self):
        # Layout principal
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Campo de entrada para o nome
        self.nome_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.nome_input)

        # Botão para gerar sugestão
        self.botao = Button(
            text="🎬 Sugerir Filme",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 0.8, 1)
        )
        self.botao.bind(on_press=self.sugerir_filme)
        self.layout.add_widget(self.botao)

        # Label para mostrar a mensagem final
        self.mensagem_label = Label(
            text="",
            font_size=18,
            halign="center",
            valign="middle"
        )
        self.layout.add_widget(self.mensagem_label)

        return self.layout

    def sugerir_filme(self, instance):
        nome = self.nome_input.text.strip()

        # Lista de filmes (com ano de lançamento para o desafio extra)
        filmes = [
            ("Matrix", 1999),
            ("Toy Story", 1995),
            ("Avatar", 2009),
            ("O Rei Leão", 1994),
            ("Homem-Aranha", 2002),
            ("Interestelar", 2014),
            ("Titanic", 1997),
            ("Jurassic Park", 1993),
            ("A Origem", 2010),
            ("Procurando Nemo", 2003),
        ]

        if not nome:
            self.mensagem_label.text = "⚠️ Por favor, digite seu nome."
        else:
            filme, ano = random.choice(filmes)
            self.mensagem_label.text = f"Olá, {nome}!\nSua sugestão de filme é: {filme} ({ano})."


if __name__ == "__main__":
    FilmeApp().run()
