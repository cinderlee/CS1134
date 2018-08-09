# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 08:56:37 2017

@author: cindylee
"""

import random

class CuckooHash ():
    def __init__ (self):
        self._T = [ None for i in range (10)]
        self._T2 = [ None for i in range (10)]
        self._r = random.random ()
        
    def __getitem__ (self, key):
        bnum = hash ((key, 0, self._r)) % len (self._T)
        bnum2 = hash ((key, 1, self._r)) % len (self._T2)
        bucket = self._T [bnum]
        bucket2 = self._T2 [bnum2]
        if bucket != None:
            if bucket [0] == key:
                return bucket [1]
        if bucket2 != None:
            if bucket2 [0] == key:
                return bucket2 [1]
            
    def __contains__ (self, key):
        bnum = hash ((key, 0, self._r)) % len (self._T)
        bnum2 = hash ((key, 1, self._r)) % len (self._T2)
        bucket = self._T [bnum]
        bucket2 = self._T2 [bnum2]
        if bucket != None:
            if bucket [0] == key:
                return True
        elif bucket2 != None:
            if bucket2 [0] == key:
                return True
        return False
            
    def __delitem__ (self, k):
        bnum = hash ((k, 0, self._r)) % len (self._T)
        bucket = self._T [bnum]
        if bucket:
            if bucket [0] == k:
                self._T[bnum] = None
        bnum2 = hash ((k, 1, self._r)) % len (self._T2)
        bucket2 = self._T2 [bnum2]
        if bucket2:
            if bucket2 [0] == k:
                self._T2 [bnum2] = None
                
    def __len__ (self):
        count = 0
        for key in range (len( self._T )): 
            if self._T [key] != None:
                count += 1
        for key in range (len (self._T2)):
            if self._T2 [key] != None:
                count += 1
        return count
        
    def keys (self):
        lst = []
        for key in range (len (self._T )): 
            if self._T [key] != None:
                lst.append( self._T [key][0])
        for key in range (len (self._T2)):
            if self._T2 [key] != None:
                lst.append ( self._T2 [key][0])
        return lst
    
    def values (self):
        lst = []
        for key in range (len (self._T )): 
            if self._T [key] != None:
                lst.append( self._T [key][1] )
        for key in range (len (self._T2)):
            if self._T2 [key] != None:
                lst.append ( self._T2 [key][1] )
        return lst
    
    def items (self):
        lst = []
        for key in range (len( self._T )): 
            if self._T [key] != None:
                lst.append ( self._T [key])
        for key in range (len (self._T2)):
            if self._T2 [key] != None:
                lst.append ( self._T2 [key])
        return lst
        
    def __iter__(self):
        for key in range (len( self._T )): 
            if self._T [key] != None:
                yield self._T [key]
        for key in range (len (self._T2)):
            if self._T2 [key] != None:
                yield self._T2 [key]
    
    def __setitem__ (self, k, v):
        location = self._T
        length = len (self._T)
        count = 0
        key = k
        value = v
        boo = False
        while boo == False and count < 2*length:
            if location is self._T:
                bucket = self._T [hash ((key, 0, self._r)) % len (self._T)]
                if bucket == None:
                    self._T[hash ((key, 0, self._r)) % len (self._T)] = (key, value)
                    boo = True
                    break 
                else:
                    value = bucket [1] 
                    key = bucket [0]
                    self._T[hash ((key, 0, self._r)) % len (self._T)] = (key, value)
                    count += 1
                    location = self._T2
            else:
                bucket2 = self._T2 [hash ((key, 1, self._r)) % len (self._T2)]
                if bucket2 == None:
                    self._T2[hash ((key, 1, self._r)) % len (self._T2)] = (key, value)
                    boo = True
                    break 
                else:
                    value = bucket2[1]
                    key = bucket2[0]
                    self._T2[hash ((key, 1, self._r)) % len (self._T2)] = (key, value)
                    count += 1
                    location = self._T
        if boo == False and count == 2*length:
            item = []
            for stuff in self:
                item.append (stuff)
            #item.append ((key, value))
            resize = [None for i in range (2*length)]
            resize2 = [None for i in range (2*length)]
            self._T = resize
            self._T2 = resize2
            self._r = random.random()
            for stuff in item:
                self.__setitem__ (stuff [0], stuff [1])
           
T=CuckooHash()
for i in range(10):
    T[i]=i*i
for i in T.keys():
    T[i]=T[i]+1
for i in range(5,10):
    if i in T:
        del T[i]
K=list(T.items())
K.sort()
print(K)
print(len(K))
print (T[0] + 1)
print (3 in T)
        
            