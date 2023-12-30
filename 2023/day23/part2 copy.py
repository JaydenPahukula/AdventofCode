from collections import deque
import sys

sys.setrecursionlimit(10000)

traversable = ".^v<>"

def solution():

    with open("input.txt", "r") as file:
        grid = [x.replace('\n','') for x in file.readlines()]

    h = len(grid)
    w = len(grid[0])
    
    adjacent = [[]]
    nodes = {(1,0):0}
    visited = {(1,0)}
    endNode = [-1]

    def addNeighbors(startx,starty,parentX,parentY,currNode):
        visited.add((startx,starty))
        q = deque()
        for x1,y1 in [(startx,starty-1),(startx,starty+1),(startx-1,starty),(startx+1,starty)]:
            if (x1,y1) != (parentX,parentY) and grid[y1][x1] in traversable:
                q.append((x1,y1,2))
        while q:
            x,y,dist = q.popleft()

            if (x,y) in visited: continue
            visited.add((x,y))
            if (x,y) == (w-2, h-1):
                newNode = len(nodes)
                nodes[(x,y)] = newNode
                endNode[0] = newNode
                adjacent[currNode].append((newNode, dist))
                adjacent.append([(currNode, dist)])
                continue

            neighbors = []
            for x1,y1 in [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]:
                if x1 < 0 or x1 >= w or y1 < 0 or y1 >= h: continue
                if (x1,y1) in nodes and (x1,y1) != (startx, starty):
                    newNode = nodes[(x1,y1)]
                    adjacent[currNode].append((newNode, dist))
                    adjacent[newNode].append((currNode, dist))
                if (x1,y1) not in visited and grid[y1][x1] in traversable:
                    neighbors.append((x1,y1))
            if len(neighbors) == 0:
                pass
            elif len(neighbors) == 1:
                q.append((neighbors[0][0],neighbors[0][1],dist+1))
            else:
                newNode = len(nodes)
                nodes[(x,y)] = newNode
                adjacent[currNode].append((newNode, dist))
                adjacent.append([(currNode, dist)])
                for x1,y1 in neighbors:
                    addNeighbors(x1,y1,x,y,newNode)
    
    addNeighbors(1,0,1,-1,0)

    print(len(nodes))
    print(nodes)
    for i in range(len(adjacent)):
        print(i, adjacent[i])
    # for yy in range(h):
    #     for xx in range(w):
    #         print(nodes[(xx,yy)] if (xx,yy) in nodes else grid[yy][xx], end="")
    #     print()

    q = deque([(0,0,[False for _ in range(len(nodes))])])
    maxDist = 0
    while q:
        currNode, dist, path = q.popleft()
        # print(currNode, dist, path)
        path[currNode] = True

        if currNode == endNode[0]:
            maxDist = max(maxDist, dist)
            #print("done", dist)
            continue
            
        for neighbor, neighborDist in adjacent[currNode]:
            if not path[neighbor]:
                q.append((neighbor, dist+neighborDist, path.copy()))
        

    return maxDist


print(solution())


# too low 6698