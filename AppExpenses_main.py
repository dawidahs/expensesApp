from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='DHS Accountancy -1')

if __name__ == '__main__':
    MyApp().run()