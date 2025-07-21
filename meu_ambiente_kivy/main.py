from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle, Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
import random

class MyPaintWidget(Widget):
    def __init__(self, **kwargs):
        super(MyPaintWidget, self).__init__(**kwargs)
        self.line_width = 2  # Espessura padrão da linha
        self.current_shape = 'line'  # Forma padrão
        self.start_pos = None  # Para armazenar posição inicial de formas
        self.current_shape_obj = None  # Para armazenar a forma atual sendo desenhada

    def on_touch_down(self, touch):
        # Gerar cor aleatória para cada novo traço
        r = random.random()
        g = random.random()
        b = random.random()
        
        with self.canvas:
            Color(r, g, b)
            
            if self.current_shape == 'line':
                # Para linhas, começamos uma nova linha
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_width)
            elif self.current_shape == 'rectangle':
                # Para retângulos, armazenamos a posição inicial
                self.start_pos = (touch.x, touch.y)
                self.current_shape_obj = Rectangle(pos=self.start_pos, size=(1, 1))
            elif self.current_shape == 'ellipse':
                # Para elipses, similar aos retângulos
                self.start_pos = (touch.x, touch.y)
                self.current_shape_obj = Ellipse(pos=self.start_pos, size=(1, 1))

    def on_touch_move(self, touch):
        if self.current_shape == 'line':
            # Para linhas, apenas adicionamos pontos
            touch.ud['line'].points += [touch.x, touch.y]
        elif self.current_shape in ['rectangle', 'ellipse'] and self.start_pos:
            # Para retângulos e elipses, calculamos tamanho e posição
            start_x, start_y = self.start_pos
            width = touch.x - start_x
            height = touch.y - start_y
            
            # Ajustamos posição e tamanho conforme o movimento
            if width < 0:
                new_x = touch.x
                width = abs(width)
            else:
                new_x = start_x
                
            if height < 0:
                new_y = touch.y
                height = abs(height)
            else:
                new_y = start_y
                
            self.current_shape_obj.pos = (new_x, new_y)
            self.current_shape_obj.size = (width, height)

    def clear_canvas(self, instance):
        self.canvas.clear()
        
    def set_line_width(self, instance, value):
        self.line_width = value
        
    def set_shape(self, shape):
        self.current_shape = shape

class MyPaintApp(App):
    def build(self):
        # Layout principal
        layout = FloatLayout()
        
        # Widget de pintura (ocupa toda a tela)
        self.paint_widget = MyPaintWidget()
        layout.add_widget(self.paint_widget)
        
        # Layout para controles (parte superior)
        controls_layout = BoxLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})
        
        # Botão para limpar
        clear_btn = Button(text='Limpar', size_hint=(None, None), size=(100, 50))
        clear_btn.bind(on_release=self.paint_widget.clear_canvas)
        
        # Slider para espessura da linha
        slider = Slider(min=1, max=20, value=2, size_hint=(0.3, None), height=50)
        slider.bind(value=self.paint_widget.set_line_width)
        
        # Botões de seleção de forma
        line_btn = ToggleButton(text='Linha', group='shape', state='down')
        rect_btn = ToggleButton(text='Retângulo', group='shape')
        ellipse_btn = ToggleButton(text='Elipse', group='shape')
        
        line_btn.bind(on_press=lambda x: self.paint_widget.set_shape('line'))
        rect_btn.bind(on_press=lambda x: self.paint_widget.set_shape('rectangle'))
        ellipse_btn.bind(on_press=lambda x: self.paint_widget.set_shape('ellipse'))
        
        # Adicionando controles ao layout
        controls_layout.add_widget(clear_btn)
        controls_layout.add_widget(slider)
        controls_layout.add_widget(line_btn)
        controls_layout.add_widget(rect_btn)
        controls_layout.add_widget(ellipse_btn)
        
        # Adicionando layout de controles ao layout principal
        layout.add_widget(controls_layout)
        
        return layout

if __name__ == '__main__':
    MyPaintApp().run()
            
         
