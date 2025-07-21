from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
    
class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def bounce_paddle(self, paddle):
        if self.collide_widget(paddle):
            offset = (self.center_y - paddle.center_y) / (paddle.height / 2)
            bounced = Vector(-1 * self.velocity_x, self.velocity_y + offset * 5)
            self.velocity = bounced 

class PongPaddle(Widget):
    score = NumericProperty(0)
    
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.bounce_paddle(self)

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    keys_pressed = set()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_key_down=self._on_key_down)
        Window.bind(on_key_up=self._on_key_up)

    def _on_key_down(self, window, key, scancode, codepoint, modifiers):
        self.keys_pressed.add(key)

    def _on_key_up(self, window, key, scancode):
        self.keys_pressed.discard(key)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = Vector(*vel)  # Começa reta, sem desvio

    def update(self, dt):
        self.ball.move()

        # Movimento do player1 (W e S)
        if 119 in self.keys_pressed:  # W
            self.player1.y = min(self.height - self.player1.height, self.player1.y + 10)
        if 115 in self.keys_pressed:  # S
            self.player1.y = max(0, self.player1.y - 10)

        # Movimento do player2 (setas ↑ e ↓)
        if 273 in self.keys_pressed:  # UP
            self.player2.y = min(self.height - self.player2.height, self.player2.y + 10)
        if 274 in self.keys_pressed:  # DOWN
            self.player2.y = max(0, self.player2.y - 10)

        # Rebote nas bordas superior e inferior
        if self.ball.y < 0:
            self.ball.y = 0
            self.ball.velocity_y *= -1
        elif self.ball.top > self.height:
            self.ball.top = self.height
            self.ball.velocity_y *= -1

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # Pontuação
        if self.ball.right < 0:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        elif self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    PongApp().run()