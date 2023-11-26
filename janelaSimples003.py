from kivy.app import App
from kivy.uix.widget import Widget

class JanelaVazia(Widget):
    pass

class MinhaApp(App):
    def build(self):
        return JanelaVazia()

if __name__ == '__main__':
    MinhaApp().run()