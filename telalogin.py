from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation = "vertical", padding = [45, 45])
        title = Label(text = 'LOGIN', font_size = 50)
        layout.add_widget(title)
        title_usuario = Label(text = 'Nome de usuário:')
        layout.add_widget(title_usuario)
        caixa_usuario = TextInput(hint_text = 'Digite seu usuário...')
        layout.add_widget(caixa_usuario)
        title_senha =  Label(text = 'Senha:')
        layout.add_widget(title_senha)
        caixa_senha =  TextInput(hint_text = 'Digite sua senha...')
        layout.add_widget(caixa_senha)
        botao = Button(text = 'Fazer Login', background_color = (0, 0, 128))
        layout.add_widget(botao)
        botao2 = Button(text = 'Já possuo uma conta', background_color = (255, 0, 0))
        layout.add_widget(botao2)

        return layout
        
if __name__ == '__main__':
    MyApp().run()