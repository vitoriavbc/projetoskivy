from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import Ellipse, Rectangle
from kivy.core.window import Window

# Definindo a classe da Bola (agora redonda)
class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        
    def bounce_paddle(self, paddle):
        if self.collide_widget(paddle):
            vx, vy = self.velocity
            offset = (self.center_y - paddle.center_y) / (paddle.height / 2)
            bounced = Vector(-vx, vy)
            vel = bounced * 1.1  # Aumenta um pouco a velocidade a cada rebatida
            self.velocity = vel.x, vel.y + offset * 2

# Definindo a classe da Raquete (Player)
class PongPaddle(Widget):
    score = NumericProperty(0)
    player_name = StringProperty("")
    
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset * 2

# Definindo a classe principal do jogo
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    score_label = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        
        # Configurações iniciais dos jogadores
        self.player1.player_name = "Player 1"
        self.player2.player_name = "Player 2"
        
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
        
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        # Movimento do Player 1 (W e S)
        if keycode[1] == 'w':
            self.player1.center_y += 20
        elif keycode[1] == 's':
            self.player1.center_y -= 20
            
        # Movimento do Player 2 (seta para cima e para baixo)
        elif keycode[1] == 'up':
            self.player2.center_y += 20
        elif keycode[1] == 'down':
            self.player2.center_y -= 20
            
        return True
    
    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel
        
    def update(self, dt):
        self.ball.move()
        
        # Colisão com as paredes superior e inferior
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
            
        # Colisão com as raquetes
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        
        # Pontuação
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball((4, 0))
        if self.ball.right > self.right:
            self.player1.score += 1
            self.serve_ball((-4, 0))
        
        # Atualiza o placar
        if hasattr(self, 'score_label'):
            self.score_label.text = f"{self.player1.player_name}: {self.player1.score}  {self.player2.player_name}: {self.player2.score}"

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    PongApp().run()