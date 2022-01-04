import tkinter as Tkinter
import math
import time

class main(Tkinter.Tk):
    def __init__(self):
        self.x = 150
        self.y = 150
        self.length = 50 # clock hand length
        self.create_all_function_trigger()
    
    def create_all_function_trigger(self):
        self.create_canvas_for_shapes()
        self.create_background()
        self.create_sticks()
        return

    def create_background(self):
        