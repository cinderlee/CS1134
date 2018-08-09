# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 21:52:16 2017

@author: cindylee
"""

class Stack ():
    def __init__ (self):
        self._A = []
    def push (self, x):
        self._A.append (x)
    def pop (self):
        return self._A.pop ()
    def top (self):
        return self._A [-1]
    def is_empty (self):	
        return self._A.is_empty ()
    def __len__(self):
        return len (self._A)


def words_keep_numbers_flip(lst):
    x = Stack ()
    for i in lst:
        if isinstance (i, int):
            x.push (i)
    counter = 0
    while counter < len (lst):
        if isinstance(lst[counter],str):
            if counter > 0 and isinstance (lst[counter - 1], int):
                lst [counter - 1], lst [counter] = lst [counter], lst [counter - 1]
                counter -=1
            else:
                counter += 1
        else:
            counter += 1
    total = len (x)
    for i in range (total, 0, -1):
        lst [len(lst) - i] = x.pop()
    
    
L1 = ["keep", 3, 2, "this", "order", 1]
L2 = ["potatoes", 3, 4, 5, "are", 9, "great"]
L3 = ["potatoes", "are", "great"]
L4 = [1, 4, 6, "hello"]

words_keep_numbers_flip (L1)
words_keep_numbers_flip (L2)
words_keep_numbers_flip (L3)
words_keep_numbers_flip (L4)

print (L1)
print (L2)
print (L3)
print (L4)