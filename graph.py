class Graph(dict):
    def __init__(self, vs=[], es=[]):
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        self[v] = {}

    def add_edge(self, e):
        v,w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v, w):
        try:
            if self[v][w]:
                return self[v][w]
        except KeyError:
            return None

    def remove_edge(self, e):
        v, w = e
        if self.get_edge(v, w):
            del self[v][w]
            del self[w][v]
        else:
            pass

    def vertices(self):
        vs = []
        for i in self:
            vs.append(i)
        return sorted(vs)
            
    def edges(self):
        es = []
        for i in self:
            for j in self[i]:
                if not self[i][j] in es:
                    es.append(self[i][j])
        return sorted(es)

    def out_vertices(self, v):
        v_adjacent = []
        for i in self[v]:
            v_adjacent.append(i)
        return v_adjacent

    def out_edges(self, v):
        e_adjacent = []
        for i in self[v]:
            e_adjacent.append(self[v][i])
        return e_adjacent
    
    def add_all_edges(self):
        for i in self.vertices():
            for j in self.vertices():
                if i != j: 
                    self.add_edge(Edge(j, i))

class Vertex(object):
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return "Vertex(%(label)s)" % {'label':repr(self.label)}

    __str__ = __repr__

class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        return "Edge(%(e1)s,%(e2)s)" % {'e1':repr(self[0]), 'e2':repr(self[1])}

    __str__ = __repr__

def main():
    v = Vertex('v')
    w = Vertex('w')
    e = Edge(v, w)
    print v, w, e

    g = Graph([v, w], [e])
    print g

if __name__ == '__main__':
    main()

