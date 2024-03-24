from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.clock import Clock

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._setup_game()
        Clock.schedule_interval(self.update, 1.0 / 60.0)  # Schedule game updates at 60 FPS

    def _setup_game(self):
        # Set up your game here (e.g., initialize game variables, set up graphics)
        self._draw_car()

    def _draw_car(self):
        # Example of drawing a simple car (a rectangle for now)
        # with self.canvas:
        #     Color(1, 0, 0)  # Red color
        #     self.car = Rectangle(pos=(self.center_x, self.y), size=(50, 100))
        self.car = Image(source='game/assets/Car.png', size_hint=(None, None), size=(Window.size.x * 0.1, Window.size.y * 0.1))
        self.add_widget(self.car)

    def update(self, dt):
        # Update your game logic here
        pass

class CarGameApp(App):
    def build(self):
        # Dynamically adjust the size to the device's dimensions
        Window.size = (360, 640)  # This could be set to any default value
        game_widget = GameWidget()
        return game_widget

if __name__ == '__main__':
    CarGameApp().run()
