import random

class PQ:
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_data', '_left', '_right' # streamline memory usage
    
        def __init__(self, data, left=None, right=None):
            self._data = data
            self._left = left
            self._right = right
            
    def __init__ (self , x = None):
        self._root = None
        
    def is_empty (self):
        return self._root == None
    def merge(self, p):
        newheap = PQ ()
        p1 = self._root 
        p2 = p._root
        if p1 == None:
            return p
        if p2 == None:
            return self
        if p1._data < p2._data: 
            newheap._root = p1
            newheap._root._left = None
            p1 = p1._left
        else:
            newheap._root = p2
            newheap._root._left = None
            p2 = p2._left
        x = newheap._root
        while x and (p1 or p2):
            if p1 and p2:
                if p1._data < p2._data:
                    x._left = p1
                    x._left._left = None
                else: 
                    x._left = p2
                    x._left._left = None
                x = x._left
            elif p1:
                x._left = p1
                break
            else:
                x._left = p2 
                break
        newheap.flip (newheap._root)
        return newheap
    
        # firsttree = PQ ()
        # secondtree = PQ()
        # extracted = PQ()
        # if p._root._data > q._root._data:
        #     firsttree._root = q._root
        #     secondtree._root = p._root
        # else:
        #     firsttree._root = p._root
        #     secondtree._root = q._root
        # extracted._root = firsttree._root._left 
        # firsttree._root._left = None
        # x = firsttree._root
        # while x and (not extracted.is_empty() or not secondtree.is_empty()):
        #     if not extracted.is_empty () and not secondtree.is_empty ():
        #         if extracted._root._data > secondtree._root._data:
        #             savetree = PQ()
        #             savetree._root = secondtree._root._left
        #             secondtree._root._left = None
        #             x._left = secondtree._root
        #             secondtree._root = savetree._root
        #         else:
        #             savetree = PQ()
        #             savetree._root = extracted._root._left
        #             extracted._root._left = None
        #             x._left = extracted._root
        #             extracted._root = savetree._root
        #     elif not extracted.is_empty ():
        #         x._left = extracted._root
        #         break
        #     else:
        #         x._left = secondtree._root
        #         break
        #     x = x._left
        # return firsttree
        
    def flip (self, root):
        if root._left != None:
            root._left, root._right = root._right, root._left
            self.flip (root._left)
            #self.flip (root._right)
        
    def insert (self, x):
        newheap = PQ ()
        newheap._root = newheap._Node (x)
        if self._root == None:
            print ('yay')
            self._root = self._Node (x)
            print (self._root._data)
        else:
            print ('nay')
            self = self.merge (newheap)
        
    def extractMin(self):
        data = self._root._data
        left_pq = PQ()
        left_pq._root = self._root._left
        right_pq = PQ()
        right_pq._root = self._root._right
        self._root._left = None
        self._root._right = None
        new_pq = left_pq.merge (right_pq)
        self = new_pq
        self._root = new_pq._root
        return data 
    
def draw_tree (node,level=1,x=20,parx=None,pary=None):
    XSEP=800
    YSEP=800
    fill(0)
    textAlign(CENTER,CENTER)
    textSize(15)
    lsize=subtree_size(node._left)
    myx,myy=x+lsize*XSEP,YSEP*level
    text(str(node._data),myx,myy)
    if node._left is not None:
        draw_tree(node._left,level+1,x,myx,myy)
    if node._right is not None:
        draw_tree(node._right,level+1,x+(lsize+1)*XSEP,myx,myy)
    if parx is not None:
        strokeWeight(10)
        stroke(0,255,0,30)
        line(parx,pary,myx,myy)
            
def subtree_size(node):
    if node is None:
        return 0
    else:
        return 1+subtree_size(node._left)+subtree_size(node._right)

def setup ():
    size (800,800)
    global pq 
    pq = PQ()
    A=list(range(20))
    random.shuffle(A)
    for i in A:
        pq.insert(i)
    print([pq.extractMin() for i in range(20)])
def draw ():
    global pq
    #draw_tree (pq._root)
    
# A=list(range(20))
# random.shuffle(A)
# pq=PQ()
# for i in A:
#     pq.insert(i)
# print (pq._root._data)
# print (pq._root._left._data)
# print (pq._root._left._left._data)
# print (pq._root._left._left._left._data)
# draw_tree (pq._root)
#print([pq.extractMin() for i in range(20)])