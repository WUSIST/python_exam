graph = {
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','F'],
    'E':'C',
    'F':'D'
}

# seen = set('A')
# queue = ['A']
# while len(queue)>0:
#     vetor = queue.pop(0)#pop(0):BFS  pop():DFS
#     for item in graph[vetor]:
#         if item not in seen:
#             queue.append(item)
#             seen.add(item)
#     print(vetor)
s = 'A'
seen = set()
queue = []
parent = {}
seen.add(s)
queue.append(s)
parent= {s:None} #s的前一个字符为空
while len(queue)>0:
    vetor = queue.pop(0)
    for item in graph[vetor]:
        if item not in seen:
            queue.append(item)
            seen.add(item)
            parent[item] = vetor #item的前一个字符为vetor
            
    print(vetor)
v = 'D'
while v!= None:
    print(v)
    v = parent[v]
