import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner


class FilmeGeneroApp(App):
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

        # Spinner para escolher o gênero
        self.spinner = Spinner(
            text="Escolha o gênero",
            values=("Ação", "Comédia", "Animação"),
            size_hint=(1, 0.2),
            background_color=(0.3, 0.6, 0.9, 1)
        )
        self.layout.add_widget(self.spinner)

        # Botão para sugerir filme
        self.botao_sugerir = Button(
            text="🎬 Sugerir Filme",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.8, 0.4, 1)
        )
        self.botao_sugerir.bind(on_press=self.sugerir_filme)
        self.layout.add_widget(self.botao_sugerir)

        # Botão para limpar
        self.botao_limpar = Button(
            text="🧹 Limpar",
            size_hint=(1, 0.2),
            background_color=(0.9, 0.3, 0.3, 1)
        )
        self.botao_limpar.bind(on_press=self.limpar)
        self.layout.add_widget(self.botao_limpar)

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
        genero = self.spinner.text

        # Listas de filmes com ano
        filmes_acao = [
            ("Matrix", 1999),
            ("John Wick", 2014),
            ("Mad Max: Estrada da Fúria", 2015),
            ("Gladiador", 2000),
        ]
        filmes_comedia = [
            ("As Branquelas", 2004),
            ("Se Beber, Não Case", 2009),
            ("Ace Ventura", 1994),
            ("Click", 2006),
        ]
        filmes_animacao = [
            ("Toy Story", 1995),
            ("Shrek", 2001),
            ("O Rei Leão", 1994),
            ("Procurando Nemo", 2003),
        ]

        if not nome:
            self.mensagem_label.text = "⚠️ Por favor, digite seu nome."
            return

        if genero == "Escolha o gênero":
            self.mensagem_label.text = "⚠️ Por favor, selecione um gênero."
            return

        # Escolhe a lista de acordo com o gênero
        if genero == "Ação":
            filme, ano = random.choice(filmes_acao)
        elif genero == "Comédia":
            filme, ano = random.choice(filmes_comedia)
        elif genero == "Animação":
            filme, ano = random.choice(filmes_animacao)
        else:
            self.mensagem_label.text = "⚠️ Gênero inválido."
            return

        self.mensagem_label.text = f"Olá, {nome}!\nSua sugestão de filme de {genero} é: {filme} ({ano})."

    def limpar(self, instance):
        """Reseta os campos para o estado inicial"""
        self.nome_input.text = ""
        self.spinner.text = "Escolha o gênero"
        self.mensagem_label.text = ""


if __name__ == "__main__":
    FilmeGeneroApp().run()
