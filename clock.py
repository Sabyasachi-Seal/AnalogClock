try:
	import Tkinter
except:
	import tkinter as Tkinter
import math
import time
class main(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
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
        self.image = Tkinter.PhotoImage(file='clock.gif')
        self.canvas.create_image(150, 150, image=self.image)
        return

    def create_canvas_for_shapes(self):
        self.canvas = Tkinter.Canvas(self, bg='black')
        self.canvas.pack(expand='yes', fill='both')
        return

    def create_sticks(self):
        self.sticks = []
        for i in range(3):
            store = self.canvas.create_line(self.x, self.y, self.x+self.length,self.y+self.length,width=2, fill='red')
            self.sticks.append(store)
        return
    
    def update_class(self):
        now = time.localtime()
        t = time.strptime(str(now.tm_hour), "%H")
        hour = int(time.strftime("%I", t))*5
        now = (hour, now.tm_min, now.tm_sec)
        # followling loop is for updating stick position
        for n,i in enumerate(now):
            x, y = self.canvas.coords(self.sticks[n])[0: 2]
            cr = [x, y]
            cr.append(self.length*math.cos(math.radians(i*6)-math.radians(90))+slef.x)
            cr.append(self.length*math.sin(math.radians(i*6)-math.radians(90))+self.y)
            self.canvas.coords(self.sticks[n], tuple(cr))
        return

if __name__ == '__main__':
    root = main()
    while True:
        root.update()
        root.update_idletasks()
        root.update_class()
    