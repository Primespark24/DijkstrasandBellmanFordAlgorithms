#had to import for system.maxsize as float("inf") wasnt working for the problem
import sys

#get user input file and format it for use in the problem
with open('rosalind_bf.txt') as file:
    vertices, edges = map(int, file.readline().strip().split(" "))
    graph = {x:{} for x in range(1, vertices + 1)}
    for line in file:
        vertex1, vertex2, weight = map(int, line.strip().split(" "))
        graph[vertex1][vertex2] = weight


def Algorithm(graph, vertex, start):
    distance = {i:sys.maxsize for i in graph}
    distance[start] = 0
    last =  {i:None for i in graph}

    #check all edges
    for i in range(vertex - 1):
        for x in graph:
            #try to keep from going to infinity
            if distance[x] != sys.maxsize:
                for y in graph[x]:
                    if distance[y] > distance[x] + graph[x][y]:
                        distance[y] = distance[x] + graph[x][y]
                        #sets current to last so as to keep loop moving
                        last[y] = x

        #check to see if wieght is negative as bellman can do this unlike dijkstra
        for x in graph:
            if distance[x] != sys.maxsize:
                for y in graph[x]:
                    if distance[y] > distance[x] + graph[x][y]:
                        distance[y] = distance[x] + graph[x][y]
                        print("negative")
        
        return distance, last
    
#call algorithm
distance, last = Algorithm(graph, vertices, 1)

#print answers
for i in graph:
    if distance[i] == sys.maxsize:
        print("x")
    else: 
        print(distance[i])
