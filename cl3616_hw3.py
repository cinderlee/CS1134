# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 23:48:41 2017

@author: cindylee
"""

import ctypes # provides low-level arrays

class aList:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self,I=None):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
        if I:
            self.extend(I)
      

    def __len__ (self):
        """Return number of elements stored in the array."""
        return self._n
    """ textbook version
    def __setitem__ (self, i, k):
        if i > len (self):
            i = i % len (self)
        if i < 0:
            i = (len (self) % i) + i
        self._A [i] = k
        
    def __getitem__ (self, k):
        """Return element at index k."""
        if k > len (self):
            k = k % len (self)
        if k < 0:
            k = (len (self) % k) + k
        return self._A [k] # retrieve from array
    """
     def __getitem__(self,i):
        if isinstance(i,slice):
            A=MyList()
            for j in range(*i.indices(self._n)):               
                A.append(self._A[j])
            return A
        if i<0:
            i=self._n+i
        return self._A[i]

    def __setitem__(self,i,x):
        if i<0:
            i=self._n+i
        self._A[i]=x
        
    def __str__ (self):
        string = "["
        for x in range (self._n - 1):
            string += str (self._A [x]) + ", "
        #string += str (self._A [-1]) + "]"
        return string

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity: # not enough room
            self._resize (2 * self._capacity) # so double capacity
        self._A [self._n] = obj
        self._n += 1
        
    def extend(self,I):
        for x in I:
            self.append(x)
            
    def pop(self,i=-1):
        r=self[i]
        del self[i]
        return r
    
    def _resize(self, c): # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c) # new (bigger) array
        for k in range (self._n): # for each existing value
            B[k] = self._A[k]
        self._A = B # use the bigger array
        self._capacity = c

    def _make_array(self, c): # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)( )
    
    def is_empty (self):
       return self._n == 0

    
    def __iter__ (self):
        for i in range (self._n):
            yield self._A[i]
  
    def __add__ (self, B):
        newlst = aList ()
        for i in range (min (len (self), len (B))):
            newlst.append (self._A[i] + B[i])
            print (newlst)
        if len (self) < len (B):
            for j in range (len (self), len (B)):
                newlst.append (B[j])
        elif len (B) < len (self):
            for k in range (len (B), len (self)):
                newlst.append (self._A[k])
        return newlst
        
    def __iadd__ (self, B):
        for i in range (self.len()):
            self [i] = self[i] + B [i]
        if len (B) > len (self):
            for b in range (len (self), len (B)):
                self.append (B[b])
    
    def __sub__ (self, B):
        newlst = aList()
        for i in range (min (len (self), len (B))):
            newlst.append (self[i] - B[i])
        if len (self) < len (B):
            for j in range (len (self), len (B)):
                newlst.append (B[j] * -1)
        else:
            for k in range (len (B), self.len()):
                newlst.append (self[k])
        return newlst
        
    def __isub__ (self, B):
        for i in range (self.len()):
            self [i] = self[i] - B [i]
        if len (B) > len (self):
            for b in range (len (self), len (B)):
                self.append (B[b] * -1)
                
def main ():
    A = aList ([1, 2, 3])
    B = aList ([4, 5, 6])
    C = aList ()
    C.append (5)
    print (C)
    print (A)
    print (B)
    x = A + B
    print (x)
    
main ()


        