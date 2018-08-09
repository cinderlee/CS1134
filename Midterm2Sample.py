# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:10:06 2017

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
            
    def odd_iter (self):
        p = self.first ()
        while p:
            yield p.data ()
            p = self.after (p)
            if p:
                p = self.after (p)
            else:
                break
            
    def swap_forward (self, p):
        node_after = self.after (p)._node
        node_before = self.before (p)._node
        node_after._prev = node_before
        p._node._next = node_after._next
        node_after._next = p._node
        p._node._prev = node_after
        node_before._next = node_after
        p._node._next._prev = p._node
    
    def location (self, p):
        if p._plist != self or self.is_empty ():
            return None
        counter = 1
        checker = self.first()
        while checker:
            if checker == p:
                return counter
            checker = self.after (checker)
            counter += 1

    def loc (self, p):
        n = self._header
        i = 0
        while n!= p._node:
            n= n._next
            i+= 1
        return i
    
L = PList()
for i in range (10):
    L.add_last (i)
for i in L.odd_iter ():
    print (i)
    
L.swap_forward (L.after (L.first()))
for i in L.odd_iter ():
    print (i)
    
L2 = PList()
for i in range (10):
    L2.add_last ("donkey")
print (L2.location (L2.first ()))
print (L2.location (L2.last ()))
print (L2.location (L2.before (L2.last ())))

