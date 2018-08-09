# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:31:13 2017

@author: cindylee
"""

"""
Name: Cindy Lee
Net ID: cl3616
Homework 3
"""

import ctypes

class aList:
    def __init__(self,I = None):
        self._n=0
        self._capacity=1
        self._A = self._make_array(self._capacity)
        if I:
            self.extend (I)

    def __len__(self):
        return self._n

    def is_empty(self):
        return len(self) == 0

    def append(self,x):
        if self._n==self._capacity:
            self._resize(2 * self._capacity)
        self._A [self._n] = x
        self._n += 1

    def extend(self,I):
        for x in I:
            self.append(x)

    def fixindex (self, number):            
        return number % self._n

    def pop(self,i=-1):
        r = self [i]
        del self [i]
        return r

    def _resize(self,newsize):
        A=self._make_array(newsize)
        self._capacity=newsize
        for i in range(self._n):
            A[i]=self._A[i]
        self._A=A

    def _make_array(self,size):
        return (size*ctypes.py_object)()

    def __getitem__(self,i):
        if isinstance(i,slice):
            A= aList()
            for j in range(*i.indices(self._n)): 
                A.append(self._A[j])
            return A
        i = self.fixindex (i)
        return self._A[i]

    def __setitem__(self,i,x):
        i = self.fixindex (i)
        self._A [i] = x

    def __iter__(self):
        for i in range(len(self)):
            yield self._A[i]

    def __str__(self):
        return "[" +"".join( str(i)+", " for i in self[:-1]) +(str(self[-1]) if not self.is_empty() else "") + "]"

    def __delitem__(self,i):
        if isinstance(i,slice):
            A= aList()
            for j in reversed(range(*i.indices(self._n))):               
                del self[j]
        else:
            i = self.fixindex (i)
            for j in range(i,self._n-1):
                self._A[j]=self._A[j+1]
            self[-1]=None        
            self._n-=1


    def __add__(self, B):
        newlst = aList ()
        for i in range (min (len (self), len (B))):
            newlst.append (self [i] + B[i])
        if len (self) < len (B):
            for j in range (len (self), len (B)):
                newlst.append (B[j])
        elif len (B) < len (self):
            for k in range (len (B), len (self)):
                newlst.append (self [k])
        return newlst
    
        
    def __iadd__ (self, B):
        self = self + B
        return self
    
    def __sub__ (self, B):
        newlst = aList()
        for i in range (min (len (self), len (B))):
            newlst.append (self[i] - B[i])
        if len (self) < len (B):
            for j in range (len (self), len (B)):
                newlst.append (B[j] * -1)
        else:
            for k in range (len (B), len (self)):
                newlst.append (self[k])
        return newlst
        
    def __isub__ (self, B):
        self = self - B
        return self
                
    def __mul__(self,times):
        multiplied = aList()
        for i in self:
            multiplied.extend ([i] * times)
        return multiplied

    def __imul__(self,times):
        self = self * times
        return self

    def __rmul__ (self, times):
        mule = aList ()
        for x in self:
            mule.append (x * times)
        return mule
        
    def __contains__(self,x):
        for y in self:
            if x==y:
                return True
        return False

    def index(self,x):
        for i in range(len(self)):
            if self[i]==x:
                return i
        return None

    def count(self,x):
        c=0
        for y in self:
            if x==y:
                c+=1
        return c

    def remove(self,x):
        del self[self.index(x)]

    def reverse(self):
        for i in range(len(self)//2):
            self [i], self [-(i+1)] = self [-(i+1)], self [i]
        return self
            
    def revitr (self):
        for i in range (-1, -1 * self._n - 1, - 1):
            yield self [i]
            
    def select (self, indexlist):
        sublist = aList ()
        for i in indexlist:
            i = self.fixindex (i)
            sublist.append (self [i])
        return sublist
       
def main ():
    A = aList ([1, 2, 3, 4, 5, 6])
    B = aList ([4, 5, 6])
    x = A + B
    print (x)
    print (A)
    A += B
    print (A * 3)
    A *= 3
    print (A)
    
    C = aList ([1, 2, 3, 3, 4, 5])
    D = aList ([4, 5, 6])
    y = C - D
    zz = D - C
    print (y)
    print (zz)
    C -= D
    print (C)
    
    F = aList ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print (F [522])    
    print (F [3 : 5])
    print (F.reverse ())
    V = aList (F.revitr())
    print (V)
    
    hi = aList (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    print (hi.select([0,2,4]))
    print (hi.select(range(0,6,2)))
    print (hi.select ([-1, -4, -7]))
    print (hi [0:4])
    print (len (hi))

    print (hi * 5)
    bye = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n']
    print (hi + bye)    
    hi.remove ('e')
    print (hi)
    hi.pop (156)
    print (hi)
    hi.pop()
    print (hi)
    
    what = aList ([1, 2, 3])
    print (3 * what)    
    
main ()