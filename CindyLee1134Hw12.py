# -*- coding: utf-8 -*-
"""
Created on Wed May  3 03:03:51 2017

@author: cindylee
"""

"""
Name: Cindy Lee
CL3616
N12335562
"""

Scores={}
import string
for c in string.ascii_lowercase:
    Scores[c]=1
for c in string.ascii_uppercase:
    Scores[c]=2
    

def lcsScore(X, Y, Scores, a = 0, b = 0, d = None):
    if d == None:
        d = {}
        lst1 = []
        lst2 = []
        for stuff in X:
            if stuff in Scores:
                lst1.append (stuff)
        for stuff2 in Y:
            if stuff2 in Scores:
                lst2.append (stuff2)
        X = "".join (lst1)
        Y = "".join (lst2)
#        X = "".join (e for e in X if e.isalpha())
#        Y = "".join (e for e in Y if e.isalpha())
    if a == len (X) or b == len (Y):
        return ("", 0)
    if (a, b) in d:
        return d [ (a, b) ]
    if X[a] == Y[b]:
        x = lcsScore (X, Y, Scores, a + 1, b + 1 , d)
        rv = (X[a] + x[0], Scores[X[a]] + x [1])
    else:
        try1s, try1 = lcsScore (X, Y, Scores, a + 1, b, d) 
        try2s, try2 = lcsScore (X, Y, Scores, a, b + 1, d) 
        if try1 > try2:
            rv = (try1s, try1)
        else:
            rv= (try2s, try2)
    d[(a,b)]=rv
    return rv
    
        
print(lcsScore("ab cdAB C","AB Cab cd",Scores))


S1="""
  From fairest creatures we desire increase,
  That thereby beauty's rose might never die,
  But as the riper should by time decease,
  His tender heir might bear his memory:
  But thou, contracted to thine own bright eyes,
  Feed'st thy light's flame with self-substantial fuel,
  Making a famine where abundance lies,
  Thy self thy foe, to thy sweet self too cruel:
  Thou that art now the world's fresh ornament,
  And only herald to the gaudy spring,
  Within thine own bud buriest thy content,
  And tender churl mak'st waste in niggarding:
    Pity the world, or else this glutton be,
    To eat the world's due, by the grave and thee."""

S2="""  Look in thy glass and tell the face thou viewest
  Now is the time that face should form another;
  Whose fresh repair if now thou not renewest,
  Thou dost beguile the world, unbless some mother.
  For where is she so fair whose unear'd womb
  Disdains the tillage of thy husbandry?
  Or who is he so fond will be the tomb,
  Of his self-love to stop posterity?
  Thou art thy mother's glass and she in thee
  Calls back the lovely April of her prime;
  So thou through windows of thine age shalt see,
  Despite of wrinkles this thy golden time.
    But if thou live, remember'd not to be,
    Die single and thine image dies with thee."""
import sys
sys.setrecursionlimit(2000)

from timeit import default_timer as timer

start = timer()
print (lcsScore(S1,S2,Scores))
end = timer()
print(end - start)  
