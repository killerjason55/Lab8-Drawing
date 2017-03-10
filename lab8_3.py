from turtle import *
class Pole:
    def init(name, stack = [], toppos = 0, xpos = 0, ypos = 0, thickness = 30, length = 120, color = 'white'):
        self.name = name
        self.stack = stack
        self.top = toppos
        self.xpos = xpos
        self.ypos = ypos
        self.thick = thickness
        self.lenght = length
        self.color = color

    def showpole(self):
        pu()
        goto(self.posx, self.posy)
        pd()
        heading(90)
        for i in range 2:
            forward(self.thick / 2)
            left(90)
            forward(length)
            left(90)
            forward(self.thick / 2)

    def pushdisk(disk):
        pass

    def popdisk():
        pass
