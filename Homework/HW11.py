# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:10:28 2017

@author: cindylee
"""

import heapq

class Passenger:
    def __init__ (self, first, last, status, fare, bags):
        self._first = first
        self._last = last
        self._status = status
        self._fare = fare
        self._bags = bags
        self._statnum = 0
        if status == "None":
            self._statnum = 0 
        elif status == "Gold":
            self._statnum = 1
        elif status == "Silver":
            self._statnum = 2
        elif status == "Platinum":
            self._statnum = 3
        elif status == "1K":
            self._statnum = 4
        elif status == "Global Service":
            self._statnum = 5
        else:
            self._statnum = 6

    def __le__ (self, passenger):
        if self._statnum <= passenger._statnum:
            return True
        return False
            
    def __lt__ (self, passenger):
        if self._statnum < passenger._statnum:
            return True
        elif self._statnum == passenger._statnum:
            if self._bags < 1 and passenger._bags > 0 :
                return True
            elif (self._bags == passenger._bags) or (self._bags > 0 and passenger._bags > 0):
                if self._fare < passenger._fare:
                    return True
                return False
            return False
        return False
    
    def __eq__ (self, passenger):
        if self._statnum == passenger._statnum:
            if (self._bags == passenger._bags) or (self._bags > 0 and passenger._bags > 0):
                if self._fare == passenger._fare:
                    return True
                return False
            return False
        return False
        
    def fare (self):
        return self._fare
    
    def bags (self):
        return self._bags

    def status (self):
        return self._status        
    
    def first (self):
        return self._first
    
    def last (self):
        return self._last
        
    
class Flight:
    def __init__ (self, capacity):
        self._lst = []
        self._cap = capacity
        self._flag = True
        
    def board (self, passenger):
        if self._flag == True:
            size = len (self._lst)
            self._lst.append ((passenger,size))
        else:
            print ("Further calls to board have been prohibited.")
        
    def finalize (self):
        heapq.heapify (self._lst)
        self._flag = False
        
    def whoToRemove (self):
        removal = []
        while len (self._lst) > self._cap:
            smaller = None
            smallest = self._lst [0]
            l = self._lst [1]
            r = self._lst [2]
            index = 0
            if l[0] == r[0]:
                if l[1] < r[1]:
                    smaller = r
                    index = 2
                else:
                    smaller = l
                    index = 1
            elif l[0] < r[0]:
                smaller = l
                index = 1
            else:
                smaller = r
                index = 2
                
            if smallest [0] == smaller [0]:
                if smallest [1] < smaller [1]:
                    self._lst [0], self._lst [index] = self._lst [index], self._lst [0]
            elif smaller [0] < smallest [0]:
                self._lst [0], self._lst [index] = self._lst [index], self._lst [0]
            
            
#            if l <= r:
#                if l[0].status () == r[0].status ():
#                    if l[0].bags == r[0].bags or (l[0].bags () >0 and r[0].bags()) > 0:
#                        if l[0].fare () == r[0].fare ():
#                            if l[1] > r[1]:
#                                smaller = l
#                                index = 1
#                            else:
#                                smaller = r
#                                index = 2
#                        elif l[0].fare () < r[0].fare ():
#                            smaller = l
#                            index = 1
#                        else:
#                            smaller = r
#                            index = 2
#                    elif l[0].bags () < 1:
#                        smaller = l
#                        index = 1
#                    else:
#                        smaller = r
#                        index = 2
#                else:
#                    smaller = l
#                    index = 1
#            else:
#                smaller = r
#                index = 2
#            if smallest[0].status() == smaller[0].status ():
#                if smallest [0]. bags() == smaller[0].bags () or (smallest[0].bags () > 0 and  smaller[0].bags ()) > 0:
#                    if smallest[0].fare() == smaller[0].fare():
#                        if smaller[1] > smallest [1]:
#                            self._lst[0], self._lst [index] = self._lst [index], self._lst [0]
#                    elif smaller[0].fare () < smallest[0].fare ():
#                        self._lst[0], self._lst [index] = self._lst [index], self._lst [0]
#                elif smaller[0].bags () < 1:
#                    self._lst[0], self._lst [index] = self._lst [index], self._lst [0]
            removal.append (heapq.heappop (self._lst))
        return removal
            
    def __iter__ (self):
        for stuff in self._lst:
            yield (stuff [0].first(), stuff [1])
            
john = Passenger ("John", "Iacono", "Platinum", 532, 0)
abc = Passenger ("abc", "cde", "Platinum", 532, 0)
jerry = Passenger ("Jerry", "Tom", "Gold", 532, 0)
carrie = Passenger ("Carrie", "Under", "None", 10, 4)
anohana = Passenger ("Ano", "Hana", "Employee", 70, 0)
why2 = Passenger ("WHy2", "now", "None", 10, 4)
sherry = Passenger ("Sherry", "Turkle", "1K", 500, 2)
christina = Passenger ("Christina", "Zu", "Global Services", 600, 3)
why = Passenger ("WHy", "now", "None", 10, 3)

x = Flight (3)
x.board (john)
x.board (abc)
x.board (jerry)
x.board (carrie)
x.board (anohana)
x.board (why2)
x.board (sherry)
x.board (christina)
x.board (why)

print (why2 == why)
print (x)
x.finalize()
for stuff in x:
    print (stuff)
print ()
for stuff in x.whoToRemove():
    print (stuff [0].first ())