
def solution():

    #read data
    with open("day18/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    #parse data
    scan = []
    for line in data:
        scan.append([int(x) for x in line.split(',')])

    #fill in grid
    r = max(map(max, scan)) + 2
    grid = [[[False for z in range(r)] for x in range(r)] for y in range(r)]
    for x, y, z in scan:
        grid[z][y][x] = True

    #bfs to make a list of all discovered blocks
    q = [(0, 0, 0)]
    discovered = [(0, 0, 0)]
    while len(q) > 0:
        (z, y, x), *q = q
        
        if x+1 < r and not grid[z][y][x+1] and (z,y,x+1) not in discovered:
            q.append((z,y,x+1))
            discovered.append((z,y,x+1))
        if x-1 >= 0 and not grid[z][y][x-1] and (z,y,x-1) not in discovered:
            q.append((z,y,x-1))
            discovered.append((z,y,x-1))
        if y+1 < r and not grid[z][y+1][x] and (z,y+1,x) not in discovered:
            q.append((z,y+1,x))
            discovered.append((z,y+1,x))
        if y-1 >= 0 and not grid[z][y-1][x] and (z,y-1,x) not in discovered:
            q.append((z,y-1,x))
            discovered.append((z,y-1,x))
        if z+1 < r and not grid[z+1][y][x] and (z+1,y,x) not in discovered:
            q.append((z+1,y,x))
            discovered.append((z+1,y,x))
        if z-1 >= 0 and not grid[z-1][y][x] and (z-1,y,x) not in discovered:
            q.append((z-1,y,x))
            discovered.append((z-1,y,x))

    #fill in an air pockets (undiscovered blocks)
    for z in range(r):
        for y in range(r):
            for x in range(r):
                if not grid[z][y][x] and (z, y, x) not in discovered:
                    grid[z][y][x] = True
    
    #find surface area
    sa = 0
    for x, y, z in scan:
        if not grid[z][y][x+1]:
            sa += 1
        if not grid[z][y][x-1]:
            sa += 1
        if not grid[z][y+1][x]:
            sa += 1
        if not grid[z][y-1][x]:
            sa += 1
        if not grid[z+1][y][x]:
            sa += 1
        if not grid[z-1][y][x]:
            sa += 1

    return sa


print(solution())