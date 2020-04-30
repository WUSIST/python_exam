import math
import heapq

graph  = {
    'A':{'B':5,'C':1},
    'B':{'A':5,'C':2,'D':1},
    'C':{'A':1,'D':4,'B':2,'E':8},
    'D':{'B':1,'C':4,'E':3,'F':6},
    'E':{'C':8,'D':3},
    'F':{'D':6}
}

def init_distance(graph,s):
    distance = {s:0}
    for key in graph:
        if key != s:
            distance[key]=math.inf
    return distance

def dijstrct(graph,s):
    pqueue =[]
    heapq.heappush(pqueue, (0,s))
    seen = set()
    parent = {s:None}
    distance = init_distance(graph,s)
    while len(pqueue)>0:
        dist,vetor = heapq.heappop(pqueue)
        seen.add(vetor)
        nodes = graph[vetor].keys()
        for w in nodes:
            if w not in seen:
                if dist + graph[vetor][w]< distance[w]:
                    heapq.heappush(pqueue,(dist + graph[vetor][w],w))
                    parent[w]= vetor
                    distance[w] = dist + graph[vetor][w]
    return parent,distance

parent,distance = dijstrct(graph,'A')
v = 'D'
print(str(distance[v]))
while v!= None:
    print(v)
    v = parent[v]
