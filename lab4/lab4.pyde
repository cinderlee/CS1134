import random

class Grid ():
    def __init__ (self, n):
        self._n = n
        self._grid = [ [False] * n for i in range (n)]
        self.randomize () 
    
    def randomize (self):
        for i in range (len (self._grid)):
            for j in range (len (self._grid)):
                y = random.randint (0, 10)
                if y < 5:
                    self._grid [i][j] = True
                    
    def generate (self):
        for i in range (len (self._grid)):
            for j in range (len (self._grid)):
                if self._grid [i][j] == True:
                    fill (0, 0, 0)
                else:
                    fill (255, 255, 255)
                stroke (0, 0, 0)
                rect (i* (width // len (self._grid)), j * height// len (self._grid), i* (width // len (self._grid)), j * height// len (self._grid))
        self.beacon ()
        
    def beacon (self):
        for x in range (1, len (self._grid)):
            for y in range (1, len (self._grid)):
                if self._grid [x-1] [y-1] == True and self._grid [x-1] [y] == True and self._grid [x][y-1] == True:
                    if self._grid [x] [y] == False:
                        newgrid = Grid (self._n)
                        for a in range (self._n):
                            for b in range (self._n):
                                if (a != x-1 and b != y-1) and (a!= x-1 and b!= y) and (a!= x and b!= y-1) and (a!= x and b!= y):
                                    y = random.randint (0, 10)
                                    if y < 5:
                                        newgrid._grid [a][b] = True
                        newgrid._grid [x-1] [y-1] = True
                        newgrid._grid [x-1] [y] = True 
                        newgrid._grid [x] [y-1] = True
                        newgrid._grid [x] [y] = True
                        self = newgrid
        
    
                        
def main ():
    a = Grid (20)
    a.generate ()
    
"""
class Rectangle ():
    def __init__ (self, x, y, filling = None):
        self._x = x
        self._y = y
        self._on = True
        if filling == None:
            self._filling = self.changeon ()
        else:
            self._filling = filling
        fill (*self._filling)
        stroke (0, 0, 0) 
        rect (x, y, 20, 20) 
        
    
    def changeon (self): 
        y = random.randint (0, 40)
        if y < 3:
            self._on = False 
            return (0, 0, 0) 
        else:
            return (255, 255, 255)
           
    def permanentchange (self):
        if self._on == False:
            self._on = True
            fill (0, 0, 0)
            stroke (0, 0, 0)
            rect (self._x, self._y, 20, 20)
            self._on = True
    
    def mouseClicked (self):
        if get (mouseX, mouseY) == (0, 0, 0):
            new = Rectangle (self._x, self._y, (255, 255, 255))
            self = new
        else:
            new = Rectangle (self._x, self._y, (0, 0, 0))
            self = new
            
    
    def getx (self):
        return self._y
    
    def gety (self):
        return self._y
    
    def beacon (self):
        x = self.getx
        y = self.gety
        if x - 40 >= 0 and y - 40 >= 0:
            if get (x - 10, y - 10) == (0,0,0) and get (x - 10, y + 10) == (0,0,0) and get (x + 10, y - 10) == (0,0,0):
                return True


def generate ():
    for x in range (0, width, 20):
        for z in range (0, height, 20):
            rectangle = Rectangle (x, z) 
            rectangle.changeon ()
            if rectangle.beacon () == True:
                generate2 (rectangle)
        
def generate2 (rectangle):
    for x in range (0, width, 20):
        for z in range (0, height, 20):
"""
def keyPressed():
    global spaceon
    if key==" " and spaceon:
        spaceon = False
        noLoop()
    elif key == " " and not spaceon:
        spaceon = True
        loop()


def setup():
    global a 
    global count
    global spaceon
    global mouse 
    spaceon = True
    mouse = False
    size (800, 800)

     
def draw (): 
    global spaceon 
    global mouse 
    clear()
    background(255)
    main ()

