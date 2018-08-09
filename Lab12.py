# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:09:55 2017

@author: cindylee
"""
import random
def select (L, k, look = True):
    print (L)
    if len (L) <= 5 and look == True:
        L.sort ()
        return L [k]
    lst = []
    i = 0
    while i< len (L):
        lst.append (L[i:i+5])
        i+=5
    #print ("Groups:", lst)
    for stuff in lst:
        stuff.sort ()
    #print ("Sorted Groups:", lst)
    median = []
    for stuff in lst:
        if len (stuff) == 5:
            median.append (stuff[2])
        elif len (stuff) == 0:
            lst.pop()
        elif len (stuff) >= 1:
            median.append (stuff[len (stuff) // 2 - 1])
    #print ("Middles:", median)
    MOM = select (median, len (median)//2)
    #print (median)
    #print ("Median middle :", MOM)
    before = []
    after = []
    #print (before, MOM, after)
    for stuff in L:
        if stuff < MOM:
            before.append (stuff)
        if stuff > MOM:
            after.append (stuff)
    #print (before, MOM, after)
    if len (before) == k:
        return MOM
    else:
        if len (before) > k:
            return select (before, k)
        else: 
            return select (after, k - len (before) - 1)
        
    
print (select([10,1,0,11,3,9,20,12,7,8,17,6,2,14,19,18,21,16,15,13,5,4], 15))

A=list(range(222))
random.shuffle(A)
print([select(A,i) for i in range(222)])