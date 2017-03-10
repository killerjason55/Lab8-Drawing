
from turtle import *
speed(0)
class Disk:
    def __init__(self,name,x,y,h,w,color = 'red'):
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

    def __repr__(self):
        text = "Disk {}, x,y: {},{} \t h,w : {},{}".format(self.name, self.x, self.y, self.h, self.w)
        return text
        
class Pole():
    def __init__(self, name, xpos, ypos,stack = [], toppos = 0, thickness = 30, length = 120, color = 'white'):
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
        goto(self.xpos, self.top)
        pd()
        
        for i in range(2):
            forward(self.thick / 2)
            left(90)
            forward(self.lenght - self.top)
            left(90)
            forward(self.thick / 2)

    def pushdisk(self, disk):
        pu()
        goto(self.xpos, self.top)
        pd()
        disk.showdisk()
        b=self.stack
        self.stack=[]
        self.stack.append(disk)
        self.stack.extend(b)
        self.top += disk.h

    def popdisk(self):
        
        last_disk = self.stack.pop(0)
        print(last_disk)
        pu()
        goto(self.xpos, self.top - last_disk.h)
        pd()
        last_disk.cleardisk()
        self.top -= last_disk.h

        self.showpole()
        return last_disk

class Hanoi(object):
    def __init__(self,n=3,start="A",workspace="B",destination="C"):
        self.startp = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination,300,0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i),0,i*150,20,(n - i)*30))

    def move_disk(self,start,destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)

        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)

    def solve(self):
        self.move_tower(3,self.startp,self.destinationp,self.workspacep)

h = Hanoi()
h.solve()
