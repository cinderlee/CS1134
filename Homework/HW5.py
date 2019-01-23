# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 00:59:59 2017

@author: cindylee
"""

"""
Name: Cindy Lee
Net ID: cl3616
N12335562
Homework 5
"""

class LeakyStack:
    def __init__ (self, maxsize, lst = []):
        self._maxsize = maxsize
        self._lst = lst
        self._length = len (self._lst)
        self._counter = len (self)

        
    def __len__ (self):
        return self._length
        
    def push (self,x):
        if len (self) < self._maxsize and self._counter < self._maxsize:
            if len (self) > 0 and len (self._lst) > self._counter: 
                self._lst [self._counter % self._maxsize] = x
                self._length += 1
            else:
                self._lst.append (x)
                self._length += 1
        else:   
            self._lst [self._counter % self._maxsize] = x
            if len (self) < self._maxsize:
                self._length += 1
        self._counter += 1
        
    def pop (self):
        top = self._lst [(self._counter - 1) % self._maxsize]
        self._lst [(self._counter - 1) % self._maxsize] = None
        self._counter -= 1
        self._length -= 1
        return top
        
    def is_empty (self):
        return len (self) == 0
    
    def __str__ (self):
        newlst = self._lst [self._counter % self._maxsize:self._maxsize] + self._lst [: self._counter % self._maxsize]
        string = "["
        for x in range (len (newlst)):
            if newlst [x] != None:
                string += str (newlst [x]) + " "
        return string + "]"
        
        
def main ():
    x = LeakyStack (5, [1, 2, 3, 4, 5])
    print (x)
    x.push (6)
    print (x)
    x.push (7)
    print (x)
    x.push (8)
    print (x)
    x.pop()
    print (len (x))
    print (x)
    x.push (9)
    print (x)
    print (len (x))
    print (x.is_empty())    
    x.push (10)
    x.push (11)
    print (x)
    x.push (12)  
    print (x)    
    x.pop()
    print (x)
    
    y = LeakyStack (5, [])
    y.push (1)
    print (y)
    y.push (2)
    y.push (3)
    print (y)
    y.push (4)
    y.push (5)
    print (y)
    y.pop ()
    y.pop()
    print (len (y))
    print (y)
    y.push (6)
    print (y)
    print (len (y))
    y.push (7)
    print (y)
    y.push (8)
    y.push (9)
    print (y)
main ()