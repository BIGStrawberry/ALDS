import math
INFINITY = math.inf


class myQueue(list):
    def __init__(self, a = []):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)


class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):         # voor afdrukken
        return str(self.data)

    def __lt__(self, other):    # voor sorteren
        return self.data < other.data


def vertices(G):
    return sorted(G)


def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]


def clear(G):  # verwijder alle toegevoegde attributen van de nodes
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v, e)


def BFS(G, s):
    V = vertices(G)
    s.predecessor = None  # s krijgt het attribuut 'predecessor'
    s.distance = 0  # s krijgt het attribuut 'distance'
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myQueue()
    q.enqueue(s)  # plaats de startnode in de queue
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)  # plaats v in queue

def path_BFS(G, u, v):
    BFS(G, u)
    a = []
    if hasattr(v, 'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    return a


#  Practicum opdracht 5.1
def is_connected(G):
    BFS(G, vertices(G)[0])  # Set distance attributes to something else than INFINITY

    for v in G:
        if v.distance == INFINITY:  # Check if a vertex has distance attribute set to INFINITY, if so, the graph is not connected.
            return False
    return True


#  Practicum opdracht 5.2
def no_cycles(G):

    # Start BFS-algorithm
    s = vertices(G)[0]
    V = vertices(G)

    s.predecessor = None  # s krijgt het attribuut 'predecessor'
    s.distance = 0  # s krijgt het attribuut 'distance'
    for v in V:
        if v != s:
            v.distance = INFINITY
    q = myQueue()
    q.enqueue(s)  # plaats de startnode in de queue
    # End BFS-algorithm

    while q:
        u = q.dequeue() # plaats waarde q in u
        for v in G[u]:
            if v.distance == INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # Vertex gets attribute 'predecessor'
                q.enqueue(v)
            elif u.predecessor != v:  # u has already been visited by another vertex
                return False  # Geen cycle gevonden
    return True  # Cycle gevonden


#  Practicum opdracht 5.3
def get_bridges(G):
    bridges = []

    for edge in edges(G):
        # Verwijder edge
        G[edge[0]].remove(edge[1])
        G[edge[1]].remove(edge[0])

        if not is_connected(G): # Controleer of G nog steeds verbonden is
            bridges.append(edge)  #  edge is een bridge omdat G niet meer verbonden is nadat deze verwijderd is

        # Plaats edge terug
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])

    return bridges


#  Practicum opdracht 5.4
def strongly_connected(G):
    if not is_connected(G):  # Controleer of G uberhaupt connected is, zo niet kunnen we meteen False returnen
        return False

    other = {}  # Nieuwe graaf

    #  Draai de oorpronkelijke graaf om en stop deze in de nieuwe graaf; other
    for edge in edges(G):
        if edge[1] in other.keys():
            other[edge[1]].append(edge[0])
        else:
            other[edge[1]] = [edge[0]]

    return is_connected(other)  # Controleer weer of G connected is, en return het resultaat

#  Practicum opdracht 5.5a
def is_euler_graph(G):
    for v in G:
        if len(G[v]) % 2 != 0:  # Controleer of de graaf geen oneven vertexes heeft, zo ja; return False
            return False
    return True

#  Practicum opdracht 5.5b
def get_euler_circuit(G, s):
    if not is_euler_graph(G):  # Controleer of de graaf uberhaupt een euler graph is, zo niet; return
        return

    steps = [s]  # Begin bij de begin node, s

    while (G[s]):  # Loop door alle stappen van de graaf
        for temp in G[s]:
            k = temp #temp save the value
            if (s, temp) not in get_bridges(G):  # Controleer of s en temp een brug vormen, zo niet, voeg hem toe als step
                break

        steps.append(k)  # Voeg een stap toe aan de lijst
        G[s].remove(k)  # Verwijder de 'traversed' nodes
        G[k].remove(s)  # Verwijder de 'traversed' nodes
        s = k

    return steps


v = [Vertex(i) for i in range(8)]

G1 = {
    v[0]: [v[4], v[5]],
    v[1]: [v[4], v[5], v[6]],
    v[2]: [v[4], v[5], v[6]],
    v[3]: [v[7]],
    v[4]: [v[0], v[1], v[5]],
    v[5]: [v[1], v[2], v[4]],
    v[6]: [v[1], v[2]],
    v[7]: [v[3]]
}

G2 = {
    v[0]: [v[4], v[5]],
    v[1]: [v[4], v[5], v[6]],
    v[2]: [v[4], v[5], v[6]],
    v[4]: [v[0], v[1], v[5]],
    v[5]: [v[1], v[2], v[4]],
    v[6]: [v[1], v[2]],
}

G3 = {
    v[0]: [v[4], v[5]],
    v[1]: [v[4], v[6]],
    v[2]: [v[5]],
    v[3]: [v[7]],
    v[4]: [v[0], v[1]],
    v[5]: [v[0], v[2]],
    v[6]: [v[1]],
    v[7]: [v[3]],
}

G4 = {
    v[0]: [v[1], v[3]],
    v[1]: [v[0], v[2]],
    v[2]: [v[1], v[3], v[4]],
    v[3]: [v[0], v[2]],
    v[4]: [v[2], v[5], v[6]],
    v[5]: [v[4], v[6]],
    v[6]: [v[4], v[5], v[7]],
    v[7]: [v[6]],
}

G5 = {
    v[0]: [v[1]],
    v[1]: [v[2]],
    v[2]: [v[0]],
}

G6 = {
    v[0]: [v[1]],
    v[2]: [v[0], v[1]],
}

G7 = {
    v[0]: [v[1], v[2]],
    v[1]: [v[2], v[0]],
    v[2]: [v[0], v[1]],
}

G8 = {
    v[0]: [v[1], v[2]],
    v[1]: [v[0], v[3]],
    v[2]: [v[0], v[3]],
    v[3]: [v[1], v[2], v[4], v[6]],
    v[4]: [v[3], v[5], v[6], v[7]],
    v[5]: [v[4], v[6]],
    v[6]: [v[3], v[4], v[5], v[7]],
    v[7]: [v[4], v[6]],
}

print ("----------------------------------------")
print ("----------/PRINTING TEST DATA/----------")
print ("----------------------------------------")
print("Is G1 connected?:", is_connected(G1))
print("Is G2 connected?:", is_connected(G2))

print("Bevat G1 een cycle?:", no_cycles(G1))
print("Bevat G2 een cycle?:", no_cycles(G2))
print("Bevat G3 een cycle?:", no_cycles(G3))

print("Welke bridges heeft G4?:", get_bridges(G4))

print("Is G5 strongly connected?:", strongly_connected(G5))
print("Is G6 strongly connected?:", strongly_connected(G6))

print("Is G8 een Euler graaf?:", is_euler_graph(G8))

print("Wat is het Euler pad van G8 (begin @ node 0): ", get_euler_circuit(G8, v[0]))

