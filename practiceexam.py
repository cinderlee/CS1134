# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:57:29 2017

@author: cindylee
"""

def f(x,n):
    total = 0
    currentnum = 0
    if n >= 0:
        currentnum = 1
    total += currentnum
    for i in range (1, n+1):
        currentnum *= x
        total += currentnum
    return total
    
print (f(2,3))
print (f(2, 0))
print (f(3, 1))
print (f(2, -1))

def anyincommon (A, B):
    a = 0
    b = 0
    while a < len (A) and b < len (B):
        if A[a] == B[b]:
            return True
        if A[a] > B[b]:
            b += 1
        else:
            a += 1
    return False
    
A = [1, 2, 3, 38, 90]
B = [4, 5, 6, 89]

C = [3, 6, 9, 12]
D = [2, 4, 6, 8, 10, 12]

E = [5, 6, 19, 20]
F = [4, 5, 6, 7, 20, 30, 40]

print (anyincommon (A,B))
print (anyincommon (C,D))
print (anyincommon (E,F)) 


class counter:
    def __init__(self):
        self._i = 0
    def print_and_increment (self):
        print (self._i)
        self._i += 1
    
A = [counter()]*5
for c in A:
    c.print_and_increment ()
    
A = [counter() for i in range (5)]
for c in A:
    c.print_and_increment()
    
A = [0] * 5
for c in A:
    print (c)
    c = c+ 1
    

def rev2 (A):
    if len (A) == 0:
        return []
    else:
        return [A [-1]] + rev (A [ :-1])

def rev (A, i = 0, copy = False):
    if copy == False:
        A = A[ : ]
        copy = True
    if len (A) <= 1:
        return A
    if i > len (A) - i - 1:
        return A
    swap = A [ i]
    A [i ] = A [len (A) - i - 1]
    A [len (A) - i - 1] = swap
    return rev (A, i+1, copy)

x = [1, 2, 3, 4]
print (rev2 (x))
print (x)
print (rev (x))
print (x)

class Stack ():
    def __init__ (self):
        self._A = []
    def push (self, x):
        self._A.append (x)
    def pop (self):
        self._A.pop ()
    def top (self):
        return self._A [-1]
    def is_empty (self):	
        return len (self._A) == 0 
        
def revStack (A):
    x = Stack ()
    for i in range (len (A)):
        x.push (A[i])
        print (A[i])
    y = []
    while x.is_empty () == False:
        y.append (x.top())
        x.pop()
    return y

print (revStack (x))

def flipArray(A):
    B = [ [] for i in A]
    for i in A:
        for j in range (len (i)):
            B[j].append (i [j])
    return B
    
A = [ [1,2,3], [4, 5, 6], [7,8,9]]
B = flipArray (A)
print (A)
print (B)

def f2(n, i = 0):
    if n > 0:
        i = f (n-1, i )
        i = f (n- 1, i)
    print (i)
    return i + 1
    
print(f2 (2))