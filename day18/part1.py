
def solution():

    #read data
    with open("day18/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    #parse data
    scan = []
    for line in data:
        scan.append([int(x) for x in line.split(',')])

    #fill in grid
    r = max(map(max, scan)) + 1
    grid = [[[False for z in range(-1, r)] for x in range(-1, r)] for y in range(-1, r)]
    for x, y, z in scan:
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