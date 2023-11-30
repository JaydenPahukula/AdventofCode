
def drawGrid(grid):
    print()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(grid[y][x], end='')
        print()
        

def solution():

    #read data
    with open("day14/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    #parse coords
    coords = []
    for line in data:
        coords.append([(int(x.split(',')[1]),int(x.split(',')[0])) for x in line.split(" -> ")])

    #find grid bounds
    maxy = 0
    for set in coords:
        for coord in set:
            if coord[0] > maxy:
                maxy = coord[0]
    minx = 500 - maxy-2
    maxx = 500 + maxy+2
    maxy += 2

    #draw grid
    w = maxx - minx + 1
    h = maxy + 1
    grid = [['.' for x in range(w)] for y in range(h)]
    for set in coords:
        y = set[0][0]
        x = set[0][1]-minx
        grid[y][x] = '#'
        for i in range(1, len(set)):
            ty = set[i][0]
            tx = set[i][1]-minx
            while y != ty or x != tx:
                if y < ty: y += 1
                if y > ty: y -= 1
                if x < tx: x += 1
                if x > tx: x -= 1
                grid[y][x] = '#'
    #draw floor
    for x in range(w):
        grid[-1][x] = '#'


    count = 0
    while 1:

        #new particle
        y = 0
        x = 500-minx

        #if spawnpoint obscured
        if grid[y][x] == 'o':
            return count

        #fall until rest
        while 1:
            if grid[y+1][x] == '.':
                y += 1
            else:
                if grid[y+1][x-1] == '.':
                    y += 1
                    x -= 1
                elif grid[y+1][x+1] == '.':
                    y += 1
                    x += 1
                else:
                    grid[y][x] = 'o'
                    break

        count += 1

    return


print(solution())