# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 21:46:38 2017

@author: cindylee
"""

class PList:
    class _Node:
        __slots__='_data','_prev','_next'
        def __init__(self,data,prev,next):
            self._data=data
            self._prev=prev
            self._next=next
    class Position:
        def __init__(self,plist,node):
            self._plist=plist
            self._node=node
        def data(self):
            return self._node._data
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        def __ne__(self,other):
            return not (self == other)
    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Position type")
        if p._plist is not self:
            raise ValueError('p does not belong to this PList')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self,node):
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position(self,node)
    def __init__(self):
        self._head=self._Node(None,None,None)
        self._head._next=self._tail=self._Node(None,self._head,None)
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        return self._make_position(self._head._next)
    def last(self):
        return self._make_position(self._tail._prev)
    def before(self,p):
        node=self._validate(p)
        return self._make_position(node._prev)
    def after(self,p):
        node=self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        pos = self.first()
        while pos:
            yield pos.data()
            pos=self.after(pos)
    def _insert_after(self,data,node):
        newNode=self._Node(data,node,node._next)
        node._next._prev=newNode
        node._next=newNode
        self._size+=1
        return self._make_position(newNode)
    def add_first(self,data):
        return self._insert_after(data,self._head)
    def add_last(self,data):
        return self._insert_after(data,self._tail._prev)
    def add_before(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node._prev)
    def add_after(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node)
    def delete(self,p):
        node=self._validate(p)
        data=node._data
        node._prev._next=node._next
        node._next._prev=node._prev
        node._prev=node._next=node._data=None
        self._size-=1
        return data
    def replace(self,p,data):
        node=self._valdiate(p)
        olddata=node._data
        node._data=data
        return olddata
    def rev_itr(self):
        pos = self.last()
        while pos:
            yield pos.data()
            pos=self.before(pos)

class Counters:
    class _Item:
        def __init__(self, name):
            self._name=name
            self._count = 0
    class Counter:
        def __init__(self,position, posinL):
            self._position=position
            self._posinL =posinL
        def name(self):
            return self._position.data()._name
        def count(self):
            return self._position.data()._count      
    def __init__(self):
        self._L = PList()
    def new_counter(self,name):
        c = Counters._Item (name)
        if self._L.is_empty():
            p = PList ()
            p.add_last (c)
            self._L.add_last (p)
        else:
            if self._L.last().data().first().data()._count == 0:
                self._L.last().data().add_last (c)
            else:
                 p = PList ()
                 p.add_last (c)
                 self._L.add_last (p)
        return Counters.Counter (self._L.last().data().last(), self._L.last())
    def delete_counter(self,counter):
        counter._posinL.data().delete (counter._position)
        counter._position=None
        counter._posinL = None
    def increment_counter(self,counter):
        #if counter._position._plist != self._L:
         #   raise ValueError('counter does not belong to this Counter')  
        if counter._posinL._plist != self._L:
            raise ValueError ('counter does not belong to this Counter')
        before = None
        newpos = None
        counter._position.data()._count+=1
        if counter._posinL == self._L.first ():
            newp = PList()
            self._L.add_first (newp)
            before = self._L.before (counter._posinL)
            newpos = before.data().add_last (counter._position.data())
            if len (counter._position._plist) == 1:
                counter._position._plist.delete (counter._position)
                self._L.delete (counter._posinL)
            else:
                self.delete_counter (counter)
            counter._position = newpos
            counter._posinL = before
        else:
            before = self._L.before (counter._posinL)
            if before.data().first().data()._count == counter.count():
                newpos = before.data().add_last (counter._position.data())
                if len (counter._position._plist) == 1:
                    counter._position._plist.delete (counter._position)
                    self._L.delete (counter._posinL)
                else:
                    self.delete_counter (counter)
                counter._position = newpos
                counter._posinL = before
            else:
                newp = PList()
                newpos = newp.add_first (counter._position.data())
                self._L.add_before (counter._posinL, newp)
              
                if len (counter._position._plist) == 1:
                    counter._position._plist.delete (counter._position)
                    self._L.delete (counter._posinL)
                else:
                    self.delete_counter (counter)
                counter._posinL = self._L.before (counter._posinL)
                counter._position = newpos
#        before_position=self._L.before(counter._position)
#        while (before_position and 
#              before_position.data()._count
#              < counter.count()):
#            new_position=self._L.add_before(before_position,counter._position.data())
#            self._L.delete(counter._position)
#            counter._position=new_position
#            before_position=self._L.before(counter._position)
    def __iter__(self):
        position=self._L.first()
        while position:
            for stuff in position.data():
            #Counters.Counter(position)
                yield stuff
            position=self._L.after(position)
                        
#        position = self._L.first ()
#        while position:
#            for stuff in position.data():
#                yield stuff._name
#                yield stuff._count
#            position = self._L.after (position)


class Counters2:
    class _Item:
        def __init__(self,name):
            self._name=name
            self._count=0
    class Counter:
        def __init__(self,position):
            self._position=position
        def name(self):
            return self._position.data()._name
        def count(self):
            return self._position.data()._count            
    def __init__(self):
        self._L=PList()
    def new_counter(self,name):
        self._L.add_last(Counters2._Item(name))
        return Counters2.Counter(self._L.last())
    def delete_counter(self,counter):
        self._L.delete(counter._position)
        counter._position=None
    def increment_counter(self,counter):
        counter._position.data()._count+=1
        before_position=self._L.before(counter._position)
        while (before_position and 
              before_position.data()._count
              < counter.count()):
            new_position=self._L.add_before(before_position,counter._position.data())
            self._L.delete(counter._position)
            counter._position=new_position
            before_position=self._L.before(counter._position)
    def __iter__(self):
        position=self._L.first()
        while position:
            yield Counters2.Counter(position)
            position=self._L.after(position)

#
#C=Counters()           
#D=Counters()
#cc=C.new_counter("A counter in C")
#D.increment_counter(cc)
C=Counters()           
a=C.new_counter("a")
b=C.new_counter("b")
c=C.new_counter("c")
d=C.new_counter("d")
e=C.new_counter("e")
f=C.new_counter("f")
g=C.new_counter("g")
h=C.new_counter("h")
i=C.new_counter("i")
j=C.new_counter("j")

C.increment_counter (d)
C.increment_counter (e)
C.increment_counter (f)
C.increment_counter (g)
C.increment_counter (h)
C.increment_counter (i)
C.increment_counter (j)

C.increment_counter (g)
C.increment_counter (h)
C.increment_counter (i)
C.increment_counter (j)

C.increment_counter (g)
C.increment_counter (h)
C.increment_counter (i)
C.increment_counter (j)

C.increment_counter (g)
C.increment_counter (h)
C.increment_counter (i)
C.increment_counter (j)

C.increment_counter (g)
C.increment_counter (h)
C.increment_counter (i)

#D = Counters ()
#D.increment_counter (a)

for stuff in C:
    print (stuff._name, stuff._count)
    
    
D=Counters2()           
a2=D.new_counter("a")
b2=D.new_counter("b")
c2=D.new_counter("c")
d2=D.new_counter("d")
e2=D.new_counter("e")
f2=D.new_counter("f")
g2=D.new_counter("g")
h2=D.new_counter("h")
i2=D.new_counter("i")
j2=D.new_counter("j")

D.increment_counter (d2)
D.increment_counter (e2)
D.increment_counter (f2)
D.increment_counter (g2)
D.increment_counter (h2)
D.increment_counter (i2)
D.increment_counter (j2)

D.increment_counter (g2)
D.increment_counter (h2)
D.increment_counter (i2)
D.increment_counter (j2)

D.increment_counter (g2)
D.increment_counter (h2)
D.increment_counter (i2)
D.increment_counter (j2)

D.increment_counter (g2)
D.increment_counter (h2)
D.increment_counter (i2)
D.increment_counter (j2)

D.increment_counter (g2)
D.increment_counter (h2)
D.increment_counter (i2)

for stuff in D:
    print (stuff._position.data())

"""
c = Counters ()
cc = C.new_counter ("A counter in C")
dd = C.new_counter ("B counter in C") 
#C.increment_counter (cc)
ee = C.new_counter ("C counter in C")
for stuff in C:
    print (stuff._name, stuff._count)
C.increment_counter (cc)
C.increment_counter (dd)
C.increment_counter (dd)
C.increment_counter (ee)
ff = C.new_counter ("D counter in C")
D.increment_counter(cc)
for stuff in C:
    if stuff:
        print (stuff._name, stuff._count)
"""