import sys
import networkx as nx
import collections

graph = nx.Graph()

for line in sys.stdin.readlines():
    a,b = line.strip().split(')')
    #print(a,b)
    graph.add_edge(a,b)

# 

res = nx.shortest_path_length(graph,"YOU","SAN")
#print(res)
#print(graph.adj) #rappresentazione con dizionari
# for node in graph.nodes():
#     print(type(node))


''' PROVO AD IMPLPEMENTARLO IO'''
def lunghezza_cammino_breve(graph, source , target):
   
    queue = collections.deque()
    dict = {}
    visited = {}
    dict[source] = 0
    
    for node in graph.nodes():
        visited[node]=False
        if node == source:
            queue.append(node)
            dict[node] = 0
            #print(list(graph.neighbors(node)))
   
    visited[source] = True

    #print(list(graph.neighbors(source)))
    cur_node = source
    while len(queue) > 0:
        queue.popleft()
        for node in graph.neighbors(cur_node):
            if node == target:
                dict[node] = dict[cur_node] + 1 
                return dict[node]
            else:
                if visited[node] != True:
                    queue.append(node)
                    dict[node] = dict[cur_node] + 1
                    visited[node] = True
                else:
                    pass
        cur_node = queue[0]

    #print(queue)
    #print(node)
    #print(dict)
    #print(queue)

res = lunghezza_cammino_breve(graph,"COM","L")
print(res)
# test
