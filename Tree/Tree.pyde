import sys
import random
import math

def setup():
    size(1100, 800)
    background(255)
    pixelDensity(displayDensity())

def drawLineAngle(color, start, angle, length, width):
    angle += 180 # make up zero degrees
    end = (start[0] + math.sin(math.radians(angle)) * length, start[1] + math.cos(math.radians(angle)) * length)
    stroke(*color)
    if width:
        strokeWeight(width)
    else:
        noStroke()
    line(*(start + end))
    return end

def drawLeaf(location):
    stroke(0, 50, 0)
    fill(100, 255, 100)
    strokeWeight(0.5)
    ellipse(location[0],location[1], 20,20)
    if number:
        fill (0,0,0)
        textSize (10)
        text ("", location [0], location [1])
    
def drawTree(start,leaf):
    end = drawLineAngle((255,0,0),start,0,300)
    endL = drawLineAngle((0,255,255),end,25,300)
    endR = drawLineAngle((0,0,255),end,-25,300)
    if leaf:
        drawLeaf(endL)
        drawLeaf(endR)
        
def keyPressed():
    global leaf
    if key=="l":
        leaf = not leaf
    global number
    if key == "n":
        number = not number

def drawnoLeaves (start, leaf, number, angle = 0, length  = 50, width = 4):
    global count
    end = drawLineAngle((255,0,0),start,angle, length, width)
    endL = drawLineAngle((0,255,255),end,angle + 25, length - 1, width - 1)
    endR = drawLineAngle((0,0,255),end, angle - 25, length - 1 , width - 1)

    if leaf:
        drawLeaf (end)
        drawLeaf(endL)
        drawLeaf(endR)

    
    if number:
        fill (0,0,0)
        textSize (10)
        text (str (count), end [0], end [1])
        count += 1
        text (str (count), endL[0], endL [1])
        count += 1
        text (str (count), endR [0], endR [1])
        count += 1

    
    """
    if count < 6 and width > 0:
        count += 1 
        return drawnoLeaves (end, leaf, count, angle),  drawnoLeaves (endL, leaf, count, angle + 25), drawnoLeaves (endR, leaf, count, angle - 25)
    """
    if width > 2 and length > 2:
        width -= 1
        length -= 1
        return drawnoLeaves (end, leaf, number, angle, length, width),  drawnoLeaves (endL, leaf, number,angle + 25, length, width), drawnoLeaves (endR, leaf, number,  angle - 25, length, width)

def setup():
    global leaf
    global number 
    global count
    leaf=True
    number = True

def draw():
    global count
    count = 0
    clear()
    background(255)
    #drawTree((550,800),leaf)
    drawnoLeaves ((550,600), leaf, number)