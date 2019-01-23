# -*- coding: utf-8 -*-
"""
Name: Cindy Lee
Net ID: cl3616
Homework 1
"""

"""
Question 1
O(n), O(n), O(n^2), O(n), O(n^3)
"""

def merge (l1, l2):
    pos = 0
    while pos < len (l1) and pos < len (l2):
        yield l1 [pos]
        yield l2 [pos]
        pos += 1
    if pos < len (l1):
        for element in l1 [pos:]:
            yield element
    elif pos < len (l2):
        for element2 in l2 [pos:]:
            yield element2

print([i for i in merge ( range(5), range(100,105))])    
print([i for i in merge ( range(5), range(100,101))])
print([i for i in merge ( range(1), range(100,105))])

class polynomial:
    def __init__ (self, numtup):
        self._numtup = numtup
    
    def __str__ (self):
        string = ""
        expo = len (self._numtup) - 1
        for num in self._numtup:
            if expo > 0:
                string += str (num) + "x^" + str (expo) + " + "
                expo -= 1
        string += str (self._numtup [-1])
        return string
    
    def evaluate (self, value):
        total = 0
        expo = len (self._numtup) - 1
        for number in self._numtup:
            total += number * (value ** expo)
            expo -= 1
        return total

P = polynomial ((6, 2, 1, 8))
print (str (P))
print([P.evaluate (i) for i in range (10)])

def sigma (func, start, end):
    total = 0.0    
    for num in range (start, end + 1):
        total += func (num)
    return total
    
def f (n):
    return 1 / pow (2, n)
print (sigma (f, 2, 10))
