from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class InitialScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(InitialScreen, self).__init__(**kwargs)
        self.add_widget(Button(text="2020"))

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class MyApp(App):

    def build(self):
        return InitialScreen()

if __name__ == '__main__':
    MyApp().run()