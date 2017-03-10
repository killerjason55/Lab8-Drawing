from turtle import *
class Disk:
    def __init__(self,name,x,y,h,w,color):
        self.name = name
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color

    def showdisk(self):
        begin_fill()
        fd(self.w/2)
        left(90)
        fd(self.h)
        left(90)
        fd(self.w)
        left(90)
        fd(self.h)
        left(90)
        fd(self.w/2)
        color(self.color)
        end_fill()
        color("black")

    def newpos(slef,x,y):
        goto(x,y)


    def cleardisk(self):
        begin_fill()
        color("white")
        fd(self.w/2)
        left(90)
        fd(self.h)
        left(90)
        fd(self.w)
        left(90)
        fd(self.h)
        left(90)
        fd(self.w/2)
        
        end_fill()
        color("black")

a=Disk("test",0,0,10,40,"red")
a.showdisk()
a.cleardisk()
