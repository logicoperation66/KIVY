import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
import time
import datetime


class MyGrid(Widget ):

    def start(self):
        print(f'Początek pracy: {time.strftime("%H:%M:%S")}')

    def end(self):
        print(f'Koniec pracy: {time.strftime("%H:%M:%S")}')

    def now_is(self):
        datetime.date.today()



class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()