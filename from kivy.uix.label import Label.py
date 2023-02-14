from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProparty

class Seconds(Label):
    done = BooleanProparty(False)

    def __init__(self, total **kwargs):
        self.done = False
        self.current = 0 
        self.total = total
        my_text = "second had past:" + str(self.current)
        super().__init__(text=my_text)
    
    def restart(self, total, **kwargs):
        self.done = False
        self.total = total
        self.current = 0
        self.text = "second had past:" + str(self.current)
        self.start()
    def start(self):
        self.value = 0 
        self.finish = False
        self.btn.text = self.btext_inprogress
        if self.autorepeat:
            self.animation.repeat = True
        self.animation.start(self.btn)
    def next(self, widget, step):
        if step == 1.0:
            self.vallue +=1
            if self.value >= self.total:
                self.animation.repeat = False
                self.finished = True