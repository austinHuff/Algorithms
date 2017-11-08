from graph import *
from grid import *
'''
Given an adjacency matrix this program implements
Dijkstra's algorithm
'''
adjMat = [
[0,2432,450,0,2334,739,0,0,449,0,817],
[2432,0,2816,2469,0,3041,2799,0,0,2839,0],
[450,2816,0,358,2765,0,220,187,220,0,1242],
[0,2469,358,0,2435,0,0,399,358,381,0],
[2334,0,2765,2435,0,0,2784,2729,0,2790,0],
[739,3041,0,0,0,0,608,0,608,380,1552],
[0,2799,220,0,2784,608,0,63,1,0,0],
[0,0,187,399,2729,0,63,0,0,217,1225],
[449,0,220,358,0,608,1,0,0,246,0],
[0,2839,0,381,2790,380,0,217,246,0,0],
[817,0,1242,0,0,1552,0,1225,0,0,0]]

g = LinkedDirectedGraph()

for i in range(0,len(adjMat)):
    g.addVertex(str(i))

for i in range(0,len(adjMat)):
    for j in range(0,len(adjMat)):
        if adjMat[i][j] != 0:
            g.addEdge(str(i),str(j),adjMat[i][j])


def dijkstra(start,graph):
    """Initialization Step"""
    inf = 1E100

    results = Grid(len(graph),3,"None")
    included = []
    for i in range(0,len(graph)):
        included.append(None)
    i = 0
    for v in graph.vertices():
        results[i][0] = v
        if str(v) == start:
            results[i][1] = 0
            results[i][2] = None
            included[i] = True
        elif graph.containsEdge(start,str(v)):
            results[i][1] = graph.getEdge(start,str(v)).getWeight()
            results[i][2] = str(start)
            included[i] = False
        else:
            results[i][1] = inf
            results[i][2] = None
            included[i] = False
        i+=1
    #print(results)
    #print(included)
    
    """Computation step"""
    while False in included:
        minimum = inf
        for i in range(0,len(included)):
            if results[i][1] < minimum and included[i] == False:
                fIndex = i
                minimum = results[i][1]
        #print(results[i][0])
        #print(included)
        included[fIndex] = True
        #print(included)
        for i in range(0,len(included)):
            if included[i] == False:
                if graph.containsEdge(str(results[fIndex][0]),str(results[i][0])):
                    newDist = results[fIndex][1] + graph.getEdge(str(results[fIndex][0]),str(results[i][0])).getWeight()
                    if newDist < results[i][1]:
                        results[i][1] = newDist
                        results[i][2] = results[fIndex][0]
    for i in range(0,len(graph)):
        for j in range(0,len(graph)):
            if str(results[j][0]) == str(i):
                #print(i)
                print(str(i) + ": dist=" + str(results[j][1]) + " parent=" + str(results[j][2]) + " included=" + str(included[i]))
                
    #print("results: \n" + "v dist parent\n" + str(results))
    #print("included: \n" + str(included))
dijkstra("0",g)
