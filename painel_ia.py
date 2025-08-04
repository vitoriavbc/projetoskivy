from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock
from kivy.lang import Builder
import random

# Carrega manualmente o arquivo .kv
Builder.load_file("painel_ia.kv")

class PainelIA(BoxLayout):
    status = StringProperty("IA Desligada")
    nivel_ameaca = NumericProperty(0)
    ia_ativa = BooleanProperty(False)

    def alternar_ia(self, estado):
        self.ia_ativa = estado
        self.status = "IA Ativa" if estado else "IA Desligada"

        if estado:
            self.simulacao_evento = Clock.schedule_interval(self.atualizar_ameaca, 1)
        else:
            if hasattr(self, 'simulacao_evento'):
                self.simulacao_evento.cancel()
            self.nivel_ameaca = 0

    def atualizar_ameaca(self, dt):
        if self.ia_ativa:
            incremento = random.randint(1, 5)
            self.nivel_ameaca = min(100, self.nivel_ameaca + incremento)

            if self.nivel_ameaca >= 80:
                self.status = "⚠ Atenção: Nível de ameaça alto!"
            elif self.nivel_ameaca >= 40:
                self.status = "IA Monitorando..."
            else:
                self.status = "IA Estável"

    def enviar_comando(self):
        comando = self.ids.campo_comando.text.strip()
        if comando == "":
            self.status = "⚠ Digite um comando válido."
        else:
            self.status = f"Comando recebido: {comando}"
            self.ids.campo_comando.text = ""

class PainelIAApp(App):
    def build(self):
        return PainelIA()

if __name__ == '__main__':
    PainelIAApp().run()
