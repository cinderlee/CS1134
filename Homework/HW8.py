# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:14:00 2017

@author: cindylee
"""

"""
Cindy Lee
Net ID: cl3616
N12335562
"""

import random


class BST:
    class _Node:
        def __init__(self,parent,left,right,data):
            self._left=left
            self._right=right
            self._parent=parent
            self._data=data
    #Question 5 Position and element 
    class Position:
        def __init__ (self, container, node):
            self._container = container
            self._node = node
        
        def element (self):
            return self._node._data
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
    
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:      # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None
    
    def __init__(self):
        self._root=None
        self._size = 0
    
    def root(self):
        return self._make_position(self._root)
    
    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)
    #Question 5 first
    def first (self):
        if self.is_empty ():
            return None
        x = self.root()
        while self.left (x):
            x = self.left (x)
        return x
    #Questin 5 last
    def last (self) :
        if self.is_empty ():
            return None
        x = self.root ()
        while self.right (x):
            x = self.right (x)
        return x
        
    def find_largestonleft (self,p):
        while self.right(p):
            p = self.right (p)
        return p
    #Question 5 before
    def before(self, p):
        if self.is_empty ():
            return None
        if p == self.first ():
            return None
        if self.left (p):
            return self.find_largestonleft (self.left (p))
        if p == self.right (self.parent (p)):
            return self.parent (p)
        else:
            while p == self.left (self.parent (p)):
                p = self.parent (p)
            return self.parent (p)
    
    def find_smallestonright (self,p):
        while self.left(p):
            p = self.left (p)
        return p
    #Question 5 after  
    def after(self, p):
        if self.is_empty ():
            return None
        if p == self.last ():
            return None
        if self.right (p):
            return self.find_smallestonright (self.right (p))
        if p == self.left (self.parent (p)):
            return self.parent (p)
        else:
            while p == self.right (self.parent (p)):
                p = self.parent (p)
            return self.parent (p)
          
    def insert(self,x):
        if self._root == None:
            self._root=BST._Node(None,None,None,x)
        else:
            self._rec_insert(self._root,x)
        self._size += 1
        
    def _rec_insert(self,n,x):
        if x<n._data:
            if n._left == None:
                n._left=BST._Node(n,None,None,x)
            else:
                self._rec_insert(n._left,x)
        else:
            if n._right == None:
                n._right=BST._Node(n,None,None,x)
            else:
                self._rec_insert(n._right,x)

    def delete(self,x):
        #Start by searching for x by setting n to the
        #node that contains x
        n=self._root
        while n and n._data != x:
            if x < n._data:
                n=n._left
            else:
                n=n._right
        #Raise an error if the search failed
        if not n:
            raise KeyError("Attempt to delete item not in BST: "+str(x))
        #Two child case
        if n._left and n._right:
            replace=n._right
            while replace._left:
                replace=replace._left
            n._data=replace._data
            n=replace
        #At this point n has 0 or 1 children
        #we set child to the child of n if it exists
        child = n._left if n._left else n._right
        # Set the child's parent pointer if it exists
        if child:
            child._parent=n._parent
        # Need to set the parent's child pointer
        # Three cases: n is the root, n is the
        # left child of its parent or n is the
        # right child of its parent
        if n is self._root:
            self._root=child
        elif n==n._parent._left:
            n._parent._left=child
        else:
            n._parent._right=child
        self._size -= 1
    
    def search_le(self,x):
        if self._root==None:
            return None
        else:
            return self._rec_search_le(self._root,x)
    def _rec_search_le(self,n,x):
        if x<n._data:
            if n._left:
                return self._rec_search_le(n._left,x)
            else:
                return None
        else:
            if n._right:
                rv=self._rec_search_le(n._right,x)
                if rv:
                    return rv
                else:
                    return n._data
            else:
                return n._data
                
    #Question 6 pos_le
    def pos_le(self,x):
        if self.root ()==None:
            return None
        else:
            return self._rec_pos_le(self.root (),x)
    
    def _rec_pos_le(self, p ,x):
        if x< p.element ():
            if self.left (p):
                return self._rec_pos_le(self.left (p),x)
            else:
                return None
        else:
            if self.right (p):
                rv=self._rec_pos_le(self.right (p),x)
                if rv:
                    return rv
                else:
                    return p
            else:
                return p
        
#    def pos_le (self, x, p = "None"):
#        if self.is_empty():
#            return None
#        if p == "None":
#            p = self.root()
#        if p.element () == x:
#            return p
#        else:
#            if x > p.element():
#                if self.right (p)== None:
#                    return p
#                else:
#                    rv = self.pos_le (x, self.right (p))
#                    if rv:
#                        return rv
#                    else:
#                        return p
#            else:
#                if self.left (p) == None:
#                    return None
#                else:
#                    rv = self.pos_le (x, self.left (p))
#                    if rv: 
#                        return rv
#                    else:
#                        return None
        
    #Question 2 search_ge (below the code done in class)
    """
    Code done in class
    def search_ge (self, x, element = "None"):
        if self.is_empty ():
            return None
        if element == "None":
            element = self._root
        if element._data == x:
            return element._data
        else:
            if element._data > x:
                if element._left == None:
                    return element._data
                else:
                    lv = self.search_ge (x, element._left)
                    if lv:
                        return lv
                    else:
                        return element._data
            else:
                if element._right == None:
                    return None
                else:
                    lv = self.search_ge (x, element._right )
                    if lv:
                        return lv
                    else:
                        return None
    """
    def search_ge(self,x):
        if self._root==None:
            return None
        else:
            return self._rec_search_ge(self._root,x)
    
    def _rec_search_ge(self,n,x):
        if x>n._data:
            if n._right:
                return self._rec_search_ge(n._right,x)
            else:
                return None
        else:
            if n._left:
                rv=self._rec_search_ge(n._left,x)
                if rv:
                    return rv
                else:
                    return n._data
            else:
                return n._data
    #Question 6 pos_ge            
    def pos_ge(self,x):
        if self.root ()==None:
            return None
        else:
            return self._rec_pos_ge(self.root (),x)
    
    def _rec_pos_ge(self,p,x):
        if x>p.element ():
            if self.right (p):
                return self._rec_pos_ge(self.right (p),x)
            else:
                return None
        else:
            if self.left (p):
                rv=self._rec_pos_ge(self.left (p),x)
                if rv:
                    return rv
                else:
                    return p
            else:
                return p
#Alternate way to do pos_ge                  
#    def pos_ge (self, x, p = "None"):
#        if self.is_empty():
#            return None
#        if p == "None":
#            p = self.root ()
#        if p.element () == x:
#            return p
#        else:
#            if p.element () > x:
#                if self.left (p) == None:
#                    return p 
#                else:
#                    lv = self.pos_ge (x, self.left (p))
#                    if lv:
#                        return lv
#                    else:
#                        return p
#            else:
#                if self.right (p) == None:
#                    return None
#                else:
#                    lv = self.pos_ge (x, self.right (p))
#                    if lv:
#                        return lv
#                    else:
#                        return None
    #Question 3
    def __len__ (self):
        return self._size 
        
    def is_empty (self):
        return len (self) == 0
        
    #Question 7 - range and pos_range
    def range (self, x,y, node = "None"):
        if self.is_empty ():
            yield None
        if node == "None":
            node = self._root
        if node._left:
            for stuff in self.range (x, y, node._left):
                yield stuff
        if node._data >= x and node._data < y:
            yield node._data
        if node._right:
            for stuff in self.range (x, y, node._right):
                yield stuff
                
    def pos_range (self, x,y, p = "None"):
        if self.is_empty ():
            yield None
        if p == "None":
            p = self.root()
        if self.left (p):
            for stuff in self.range (x, y, self.left(p)):
                yield stuff
        if p.element() >= x and p.element () < y:
            yield p
        if self.right (p):
            for stuff in self.range (x, y, self.right (p)):
                yield stuff
   
   #Question 1
    def __iter__ (self):
        node = self._root
        while node != None:
            if node._left == None:
                yield node._data
                node = node._right
            else:
                pre = node._left 
                while pre._right and (pre._right != node):
                    pre = pre._right
                if pre._right == None:
                    pre._right = node
                    node = node._left
                else:
                    pre._right = None
                    yield node._data
                    node = node._right
                    
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    
    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)
    def _height1(self):                 # works, but O(n^2) worst-case time
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):                  # time is linear in size of subtree
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p) 
        
    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:     # left child exists
            count += 1
        if node._right is not None:    # right child exists
            count += 1
        return count
    
    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0
   
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    
    def get_depth (self, d, count = 0, p = None):
        if p == None:
            p = self.root()
        if self.is_leaf (p):
            d [p.element ()].append (count)
        else:
            d[p.element ()].append (count)
            if self.left (p):
                self.get_depth (d, count + 1, self.left (p))
            if self.right (p):
                self.get_depth (d, count + 1, self.right (p))
          
    #Question 4
    def print (self, flip = False):
        d = dict ()
        depthdict = dict()
        for i in range (self.height () + 1):
            depthdict [i] = []
        for x in self:
            d [x] = []
        self.get_depth (d)
        space = 0
        lengthoflongest = len (str (self.last ().element ()))
        for x in self:
            d[x].append (space)
            space += lengthoflongest
        for x in d:
            depthdict [d[x] [0]].append ((x, d[x][1]))
        for y in depthdict:
            depthdict[y].sort (key = lambda tup: tup[1])
        string = []
        count = 0
        i = 0
        while count in depthdict:
            string2 = ""
            if len (depthdict[count]) == 1:
                string2 += str (depthdict [count][0] [0])
            else:
                while (i + 1) < len (depthdict[count]):
                    first = depthdict[count][i][1]
                    second = depthdict[count][i + 1][1]
                    string2 += str (depthdict[count][i][0]) + (int(second - first - 1 - (len (str (depthdict [count][i][0])) - 1)) * " ")
                    if i == len (depthdict[count]) - 2:
                        string2 += str (depthdict [count] [i + 1] [0])
                    i += 1
            if depthdict[count][0][1] > 0:
                string2 = (int (depthdict[count][0][1]))  * " " + string2
            string.append(string2 + "\n")
            count += 1
            i = 0 
        if flip:
            flipped = ""
            for i in range (len (string)):
                flipped = string [i] + flipped
            print (flipped)
        else:
            print ("".join(string))
    def question (self, p, lst = None):
        if lst == None:
            lst = [0,0,0]
        if self.is_leaf (p):
            lst[0] +=1
        elif self.left (p) and self.right (p):
            lst [2] += 1
            self.question (self.left (p), lst)
            self.question (self.right (p), lst)
        elif self.left (p):
            lst[1] += 1
            self.question (self.left (p), lst)
        else:
            lst [1] +=1
            self.question (self.right (p),lst)
        return lst

T=BST()
L=list(range(10,100,10))
random.shuffle(L)
for i in L:
    T.insert(i)
print ("LE TEST")
for i in range(5,105,5):
    print(T.search_le(i))
print ()
for i in range(5,105,5):
    if T.pos_le (i):
        print("POSLE of " + str (i) + ":" + str (T.pos_le(i).element ()))

print ("ITER TEST")
for i in T:
    print (i)

print ("LEN TEST: " + str(len (T)))
print ("GE TEST")
for i in range(5,105,5):
    print("GE of " + str (i) + ":" + str (T.search_ge(i)))
for i in range(5,105,5):
    if T.pos_ge (i):
        print("POSGE of " + str (i) + ":" + str (T.pos_ge(i).element ()))
print ("FIRST TEST : " + str (T.first ().element()))
print ("LAST TEST: " + str (T.last ().element()))

if (T.before (T.root())):
    print ("Before root " + str (T.root().element ()) + ": " + str (T.before (T.root()).element()))
    
print ("Range from 50 to 90")
for i in T.range (50, 90):
    print (i)
    
print ("Range from 24 to 80")
for i in T.range (0, 110):
    print (i)
    
print ("Tree print: ")
T.print ()

#Question 8
print ("Question 8")
def make_binaryfor8 (bst, p, counter):
    if counter > 0:
        bst.insert (p.element () - counter)
        bst.insert (p.element () + counter)
        make_binaryfor8 (bst, bst.left (p), counter // 2  )
        make_binaryfor8 (bst, bst.right (p), counter // 2)
        
B = BST ()
B.insert (32)
make_binaryfor8 (B, B.root (), 16)
B.print()

print ("Before 32: " + str (B.before (B.root ()).element ()))
print ("Before 16: " + str (B.before (B.left (B.root ())).element ()))
print ("After 32: " + str (B.after (B.root ()).element ()))
print ("After 48: " + str (B.after (B.right (B.root ())).element ()))
print ("POSGE of 35: " + str (B.pos_ge (35).element()))
print ("POSGE of -8: " + str (B.pos_ge (-8).element()))
print ("POSLE of 43: " + str (B.pos_le (43).element ()))
print ("POSLE of 70: " + str (B.pos_le (70).element ()))
print ("Range from 16 to 60")
for i in B.range (16, 60):
    print (i)
#print (len (B))

#Question 9
print ("Question 9")
C = BST ()
C.insert ( 11)

def make_treefor9 (bst):
    for i in range (9, -1, -1):
        bst.insert (i)

    for i in range (12, 21):
        bst.insert (i)


make_treefor9 (C)
C.print (True)

#print (len (C))
print ("Another example: ")
example = BST()
example.insert (50)
example.insert (40)
example.insert (70)
example.insert (20)
example.insert (60)
example.insert (90)
example.insert (10)
example.insert (30)
example.print ()

print (example.question (example.root()))
print ("Before 60: " + str (
example.before (example.left (example.right (example.root()))).element ()))

print ("Another example: ")
example2 = BST()
example2.insert (50)
example2.insert (30)
example2.insert (70)
example2.insert (20)
example2.insert (40)
example2.insert (65)
example2.insert (90)
example2.insert (47)
example2.insert (52)
example2.insert (80)
example2.insert (95)
example2.insert (42)
example2.insert (60)
example2.print ()
print ("Before 52: " + str (
example2.before (example2.left (example2.left (example2.right (example2.root())))).element ()))

print ("After 47: " + str (example2.after(example2.right (example2.right (example2.left (example2.root())))).element ()))

print ("Larger example to test print for numbers in 100s: ")
T2=BST()
L2=list(range(5,200,10))
random.shuffle(L2)
for i in L2:
    T2.insert(i)
    
T2.print ()