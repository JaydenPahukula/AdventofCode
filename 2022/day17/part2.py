
def addShape(grid, shapeNum:int):

    #ensure there are only 3 lines of whitespace
    while grid != [] and grid[-1] == ['.','.','.','.','.','.','.']:
        grid.pop(-1)
    grid.append(['.','.','.','.','.','.','.'])
    grid.append(['.','.','.','.','.','.','.'])
    grid.append(['.','.','.','.','.','.','.'])

    #add shapes
    if shapeNum == 0:
        grid.append(['.','.','@','@','@','@','.'])
    elif shapeNum == 1:
        grid.append(['.','.','.','@','.','.','.'])
        grid.append(['.','.','@','@','@','.','.'])
        grid.append(['.','.','.','@','.','.','.'])
    elif shapeNum == 2:
        grid.append(['.','.','@','@','@','.','.'])
        grid.append(['.','.','.','.','@','.','.'])
        grid.append(['.','.','.','.','@','.','.'])
    elif shapeNum == 3:
        grid.append(['.','.','@','.','.','.','.'])
        grid.append(['.','.','@','.','.','.','.'])
        grid.append(['.','.','@','.','.','.','.'])
        grid.append(['.','.','@','.','.','.','.'])
    else:
        grid.append(['.','.','@','@','.','.','.'])
        grid.append(['.','.','@','@','.','.','.'])

    return


def moveShape(grid, right:bool):

    #make a new grid to edit
    newgrid = []
    for row in grid:
        newgrid.append(row.copy())

    #attempt to move the piece
    for row in newgrid:
        if right:
            for x in range(6, -1, -1):
                if row[x] == '@':
                    if x == 6:
                        return False
                    if row[x+1] == '#':
                        return False
                    row[x] = '.'
                    row[x+1] = '@'
        else:
            for x in range(7):
                if row[x] == '@':
                    if x == 0:
                        return False
                    if row[x-1] == '#':
                        return False
                    row[x] = '.'
                    row[x-1] = '@'
    
    #if successful, copy the changes to the grid
    for i in range(len(newgrid)):
        grid[i] = newgrid[i].copy()
    return True


def moveDown(grid):

    #make a new grid to edit
    newgrid = []
    for row in grid:
        newgrid.append(row.copy())

    #attempt to move the piece
    for y in range(len(newgrid)):
        for x in range(7):
            if newgrid[y][x] == '@':
                if y == 0:
                    return False
                if newgrid[y-1][x] == '#':
                    return False
                newgrid[y][x] = '.'
                newgrid[y-1][x] = '@'
    
    #if successful, copy the changes to the grid
    for i in range(len(newgrid)):
        grid[i] = newgrid[i].copy()
    return True


def done(grid):
    #change the piece from movable ('@') to immovable ('#')
    for y in range(len(grid)):
        for x in range(7):
            if grid[y][x] == '@':
                grid[y][x] = '#'


def getHeight(grid):
    #get the height of the grid minus whitespace
    whitespace = 0
    for line in grid[::-1]:
        if line == ['.','.','.','.','.','.','.']:
            whitespace += 1
        else:
            break
    return len(grid)-whitespace


def solution():
    with open("day17/input.txt", "r") as file:
        data = file.readlines()[0]
    
    grid = [['.','.','.','.','.','.','.'] for y in range(3)]

    i = 0
    count = 0
    currShape = 0
    height = 0
    oldcount = 0
    addShape(grid, currShape)
    while 1:

        #read next instruction
        if data[i] == '>': right = True
        else: right = False
        i = (i+1) % len(data)

        #try to move the shape right or left
        moveShape(grid, right)

        #if the shape cant move down
        if not moveDown(grid):

            #shape is done falling
            done(grid)
            count += 1
            if count >= 1000000000000:
                return height + getHeight(grid)
            
            #look for pattern
            if i == 1 and currShape == 0:
                if oldcount == 0:
                    oldcount = count
                    oldheight = height+getHeight(grid)
                else:
                    countdiff = count-oldcount
                    heightdiff = height+getHeight(grid)-oldheight
                    while count < 1000000000000-countdiff:
                        count += countdiff
                        height += heightdiff

            #only keep the 100 most recent blocks
            while len(grid) > 100:
                height += 1
                grid.pop(0)

            #add the next shape
            currShape = (currShape+1) % 5
            addShape(grid, currShape)


    return


print(solution())


#5526 low
#7135 low