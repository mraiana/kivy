from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        txt = Label(text=' ПЕРВЫЙ ЭКРАН')
        btn = Button(text='ПЕРЕХОД НА ВТОРОЙ ЭКРАН')
        btn.on_press = self.next 
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        self.add_widget(layout) # экран - это виджет, на котором могут создаваться все другие (потомки)

    def next(self):
        self.manager.transition.direction = 'left' # объект класса Screen имеет свойство manager                                     # - это ссылка на родителя
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn1 = Button(text='ПЕРЕХОД НА ПЕРВЫЙ ЭКРАН')
        btn2 = Button(text='ПЕРЕХОД НА ТРЕТИЙ ЭКРАН')
        btn1.on_press = self.next 
        btn2.on_press = self.back 
        layout = BoxLayout()
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        self.add_widget(layout) 
        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

    def back(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'third'

class ThirdScr(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name)
        txt = Label(text='ТРЕТИЙ ЭКРАН')
        btn = Button(text='ПЕРЕХОД НА ПЕРВЫЙ ЭКРАН ')
        btn.on_press = self.next 
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        self.add_widget(layout) 
        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThirdScr())
        return sm

app = MyApp()
app.run()
