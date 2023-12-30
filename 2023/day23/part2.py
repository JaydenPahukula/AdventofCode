from collections import deque

traversable = ".^v<>"
def solution():

    with open("input.txt", "r") as file:
        grid = [x.replace('\n','') for x in file.readlines()]

    h = len(grid)
    w = len(grid[0])
    
    q = deque([(1,0,set())])
    maxDist = 0
    while q:
        x,y,path = q.popleft()
        path.add((x,y))

        if (x,y) == (w-2, h-1):
            print("done", len(path)-1)
            maxDist = max(maxDist, len(path)-1)
            continue

        if grid[y-1][x] in traversable and (x,y-1) not in path: q.append((x,y-1,path.copy()))
        if grid[y+1][x] in traversable and (x,y+1) not in path: q.append((x,y+1,path.copy()))
        if grid[y][x-1] in traversable and (x-1,y) not in path: q.append((x-1,y,path.copy()))
        if grid[y][x+1] in traversable and (x+1,y) not in path: q.append((x+1,y,path.copy()))

    return maxDist


print(solution())