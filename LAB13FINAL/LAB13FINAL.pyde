import copy
import xml.etree.ElementTree as etree

def getMap(file):
    G=open(file)
    root = etree.parse(G).getroot()
    v={}
    for child in root:
        if (child.tag=="node"):
            v[child.attrib["id"]]=(float(child.attrib["lon"]),float(child.attrib["lat"]))
    e=[]
    for child in root:
        if (child.tag=="way"):
            a=[]
            for gc in child:
                if gc.tag=="nd":
                    a.append(v[gc.attrib["ref"]])
            for i in range(len(a)-1):
                e.append((a[i],a[i+1]))
    return list(v.values()),e

class Map:
    class Graph:
        class Vertex:
            slots = "_element"
            def __init__ (self, x):
                self._element = x
            def element(self):
                return self._element
            def __hash__ (self):
                return hash (id (self))
        class Edge:
            slots = '_origin' , '_destination' , '_element'

            def __init__ (self, u, v, x):
                #Do not call constructor directly. Use Graph s insert edge(u,v,x).”””
                self._origin = u
                self._destination = v
                self._element = x

            def endpoints(self):
                #”””Return (u,v) tuple for vertices u and v.”””
                return (self._origin, self._destination)
        
            def opposite(self, v):
                #Return the vertex that is opposite v on this edge.
                return self._destination if v is self._origin else self._origin
        
            def __hash__ (self): 
                return hash( (self._origin, self._destination) )
    
            def element(self):
                #”””Return element associated with this edge.”””
                return self._element
        
        def __init__ (self, directed=False):
            self._outgoing = { }
            self._incoming = { } if directed else self._outgoing
        def is_directed(self):
            return self._incoming is not self._outgoing # directed if maps are distinct
        def vertex_count(self):
            return len(self._outgoing)
        def vertices(self):
            return self._outgoing.keys()
        def edge_count(self):
            total = sum(len(self._outgoing[v]) for v in self._outgoing)
            return total if self.is_directed( ) else total // 2
        def edges(self):
            result = set( ) 
            for secondary_map in self._outgoing.values():
                result.update(secondary_map.values()) 
            return result

        def get_edge(self, u, v):
            return self._outgoing[u].get(v) # returns None if v not adjacent
        def degree(self, v, outgoing=True):
            adj = self._outgoing if outgoing else self._incoming
            return len(adj[v])
        def incident_edges(self, v, outgoing=True):
            adj = self._outgoing if outgoing else self._incoming
            for edge in adj[v].values():
                yield edge
        def insert_vertex(self, x=None):
            v = self.Vertex(x)
            self._outgoing[v] = { }
            if self.is_directed():
                self._incoming[v] = { } 
            return v
        def insert_edge(self, u, v, x=None):
            e = self.Edge(u, v, x)
            if v in self._outgoing [u]:
                pass
            if u in self._incoming [v]:
                pass
            self._outgoing[u][v] = e
            self._incoming[v][u] = e
            
    def __init__ (self, V, E):
        self._g = self.Graph ()
        vs = {}
        for stuff in V:
            vs [stuff ] = self._g.insert_vertex (stuff)
        for stuff2 in E:
            self._g.insert_edge (vs [stuff2[0]], vs [stuff2[1]])
            
    def draw (self):
        #e = list (self._g.edges ()) [0]
        #line(e._origin._element [0], e._origin._element [1], e._destination._element [0], e._destination._element [1])
        x, y = mouseToScreen (mouseX, mouseY)
        distance = []
        for e in self._g.edges():
            stroke (0, 0, 0)
            line(e._origin._element [0], e._origin._element [1], e._destination._element [0], e._destination._element [1])
            distance.append ((min (dist (e._origin._element [0],e._origin._element[1], x, y ), dist (e._destination._element [0],e._destination._element[1], x, y )), e))
        edge = min (distance) [1]
        for e in self._g.edges ():
            if e == edge:
                strokeWeight (0.00002)
                stroke (0, 255, 0)
                line(e._origin._element [0], e._origin._element [1], e._destination._element [0], e._destination._element [1])
            else:
                strokeWeight (0.00001)
                stroke (0, 0, 0)
                line(e._origin._element [0], e._origin._element [1], e._destination._element [0], e._destination._element [1])
    def closest (self):
        x, y = mouseToScreen (mouseX, mouseY)
        something = list (self._g.edges())
        distance = min (dist (something [0]._origin._element [0],something[0]._origin._element[1], x, y ), dist (something [0]._destination._element [0],something[0]._destination._element[1], x, y ))  
        edge = something [ 0 ]
        i = 1
        while i < len (something):
            if min (dist (something [i]._origin._element [0],something[i]._origin._element[1], x, y ), dist (something [i]._destination._element [i],something[0]._destination._element[1], x, y )) < distance:
                edge = something [i]
        stroke (0, 255, 0) 
        line(edge._origin._element [0], edge._origin._element [1], edge._destination._element [0], edge._destination._element [1])

def mouseToScreen(mx,my):
    global minlon
    global minlat
    global maxlat
    global maxlon
    return (minlon+(mx/float(width))*(maxlon-minlon), minlat+(my/float(height))*(maxlat-minlat))

def BFS(g, s, discovered):
    level = [s]
    while len(level) > 0:
        next_level = [] 
        for u in level:
            for e in g.incident_edges(u): 
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v) 
        level = next_level

def setup ():
    size (800,600)
    global mapster
    global minlon
    global minlat
    global maxlat
    global maxlon
    maxlat=40.6903
    minlat=40.7061
    maxlon=-73.9728
    minlon=-74.0065
    (V,E) = getMap ("map.osm")
    mapster = Map (V, E)
    #mapster.closest ()
    
    
def draw ():
    global mapster
    global minlon
    global minlat
    global maxlat
    global maxlon
    maxlat=40.6903
    minlat=40.7061
    maxlon=-73.9728
    minlon=-74.0065
    scale(float(width)/(maxlon-minlon),float(height)/(maxlat-minlat))
    translate(-minlon,-minlat)
    strokeWeight(0.00001)
    mapster.draw()
    