from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout # макет (это тоже виджет!)
from kivy.uix.label import Label # надпись
from kivy.uix.button import Button # кнопка
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test

age = 13
name = "Timur"

p1, p2, p3 = 0,0,0

class InstrScr(Screen):
   def __init__(self, **kwargs):
      super().__init__(self, **kwargs)
      instr = Label(text=txt_instruction)
      lbl1 = Label(text="Enter Your Name:", halign="right")
      self.in_name = TextInput(multiline=False)
      lbl2 = Label(text="Enter your age:", halign="right")
      self.in_age = TextInput(text="7", multiline=False)
      self.btn = Button(text="Start", size_hint=(0.3, 0.2), pos_hint = {"center_x": 0.5})
      self.btn.on_press = self.next
      line1 = BoxLayout(size_hint=(0.3, None), height="30sp")
      line2 = BoxLayout(size_hint=(0.3, None), height="30sp")
      line1.add_widget(lbl1)
      line1.add_widget(self.in_name)
      line2.add_widget(lbl2)
      line2.add_widget(self.in_age)
      outer = BoxLayout(orientation="verical", padding = 8, spacing = 8)
      outer.add_widget(instr)
      outer.add_widget(line1)
      outer.add_widget(line2)
      outer.add_widget(self.btn)
      self.add_widget(outer)
   def next(self):
      global name
      name = self.in_name.text
      self.manager.current = "pulse1"
class PulseScr(Screen):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.next_screen = False

      instr = Label(txt_test1)
      self.lbl_sec = Seconds(15)
      self.lbl_sec.bind(done=self_finish)

      line = BoxLayout(size_hint=(0.8, None), height="30sp")
      lbl_result = Label(text="Enter results:", halign="right")
      self.in_result = TextInput(text= "0", multiline = False)
      self.in_result.set_disabled(True)
      
      line.add_widget(lbl)