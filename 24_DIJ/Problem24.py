#import to allow for "infinite" number as float("inf") isnt working for some reason
import sys

with open('rosalind_dij.txt') as file:
        vertex, edge = map(int, file.readline().strip().split(" "))
        #allows declaration of graph to work and be initilized
        graph = [[sys.maxsize] * vertex for i in range(vertex)]
        for line in file:
            vertex1, vertex2, weight = map(int, line.strip().split(" "))
            graph[vertex1 - 1][vertex2 - 1] = weight
 

def Algorithm(start, graph, vertex):
    #init to inf but multiply by vertex to allow start to be 0
    distance = [sys.maxsize] * vertex
    #no distance at start
    distance[start] = 0
    #hold/check shortest distance to point
    checked = [False] * vertex

    for i in range(vertex):
        x = ShortestDist(distance, checked)
        checked[x] = True

        for z in range(vertex):
            if graph[x][z] > 0 and checked[z] == False and distance[z] > distance[x] + graph[x][z]:
                distance[z] = distance[x] + graph[x][z]

    for i in range(vertex):
        if distance[i] < sys.maxsize:
            print(distance[i])
        else:
            print(-1)

def ShortestDist(distance, checked):
    index = sys.maxsize
    sub_index = distance.index(index)
    
    #find smallest distance from current points
    for i in range(vertex):
        if distance[i] < index and checked[i] == False:
            index = distance[i]
            sub_index = i
    return sub_index


Algorithm(0, graph, vertex)

