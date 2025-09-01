from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
import random


# --- Tela 1: Boas-Vindas ---
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)

        self.label = Label(text="Digite seu nome:", font_size=20)
        layout.add_widget(self.label)

        self.name_input = TextInput(hint_text="Seu nome aqui", multiline=False, size_hint=(1, 0.2))
        layout.add_widget(self.name_input)

        self.continue_button = Button(text="Continuar", size_hint=(1, 0.3), background_color=(0.2, 0.6, 1, 1))
        self.continue_button.bind(on_press=self.go_to_movies)
        layout.add_widget(self.continue_button)

        self.add_widget(layout)

    def go_to_movies(self, instance):
        nome = self.name_input.text.strip()
        if nome:
            self.manager.get_screen("movies").set_user_name(nome)
            self.manager.current = "movies"


# --- Tela 2: Sugestão de Filmes ---
class MovieScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)

        # Label de boas-vindas
        self.welcome_label = Label(text="Bem-vindo!", font_size=22)
        layout.add_widget(self.welcome_label)

        # Spinner para escolher gênero
        self.spinner = Spinner(
            text="Selecione um gênero",
            values=("Ação", "Comédia", "Animação"),
            size_hint=(1, 0.3),
        )
        layout.add_widget(self.spinner)

        # Botão para sugerir filme
        self.suggest_button = Button(text="Sugerir Filme", size_hint=(1, 0.3), background_color=(0.4, 0.9, 0.4, 1))
        self.suggest_button.bind(on_press=self.suggest_movie)
        layout.add_widget(self.suggest_button)

        # Label para exibir sugestão
        self.movie_label = Label(text="", font_size=20, color=(1, 0, 0, 1))
        layout.add_widget(self.movie_label)

        self.add_widget(layout)

        # Dicionário de filmes
        self.movies = {
            "Ação": ["Mad Max: Estrada da Fúria", "John Wick", "Gladiador", "Velozes e Furiosos"],
            "Comédia": ["As Branquelas", "Se Beber, Não Case", "Gente Grande", "Minha Mãe é uma Peça"],
            "Animação": ["Shrek", "Toy Story", "Procurando Nemo", "Divertida Mente"],
        }

    def set_user_name(self, name):
        self.welcome_label.text = f"Bem-vindo(a), {name}! Escolha um gênero:"

    def suggest_movie(self, instance):
        genre = self.spinner.text
        if genre in self.movies:
            movie = random.choice(self.movies[genre])
            self.movie_label.text = f"Sugestão: {movie}"
        else:
            self.movie_label.text = "Por favor, escolha um gênero válido!"


# --- Gerenciador de Telas ---
class MovieApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name="welcome"))
        sm.add_widget(MovieScreen(name="movies"))
        return sm


if __name__ == "__main__":
    MovieApp().run()
