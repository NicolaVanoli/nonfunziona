'''
NICOLA VANOLI
'''

import sys
import networkx as nx
tunnels = [] #è una lista contenente i vari tunnel
starts = [] # contiene i punti di partenza dei tunnel

dices_res =[] # contiene i lanci che ho fatto per ottenere il risultato 
box = nx.DiGraph() 
'''
INPUT
'''
n = int(sys.stdin.readline().strip())
for line in sys.stdin.readlines():
    start,end = line.rstrip().split()
    
    tunnels.append([int(start),int(end)])
for i in tunnels:
    starts.append(i[0])

"""
BUILDING GRAPH
"""

for i in range(0, n+1): #costruisco i nodi
        box.add_node(i,weight = 0)
for hole in tunnels:
        box.add_edge(hole[0], hole[1], lenght=0)
for i in range(0, n+1): #costruisco gli edges
        for dice in [1, 2, 3, 4, 5, 6]:
            if  i + dice <= n and i not in starts :  
                box.add_edge(i, i+dice, lenght=1)

minimum_dices = nx.shortest_path_length(box, 0, n, weight="lenght") #è la prima richiesta
list_of_shortest_path = [p for p in nx.all_shortest_paths(box,0,n, weight="lenght")]
while len(list_of_shortest_path)>1:
    for i in range(1,minimum_dices*2):
        if list_of_shortest_path[0][i] == list_of_shortest_path[1][i]:
            pass
        elif list_of_shortest_path[0][i] < list_of_shortest_path[1][i]:
            list_of_shortest_path.remove(list_of_shortest_path[1])
            break
        else:
            list_of_shortest_path.remove(list_of_shortest_path[0])
            break
path = list_of_shortest_path[0]
for i in range(1, len(path)):
    if [path[i-1], path[i]] not in tunnels:
        dices_res.append(str(path[i]-path[i-1]))

res1 = minimum_dices
res2 = " ".join(dices_res)

print(res1)
print(res2)
