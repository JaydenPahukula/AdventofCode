# N0TE: This takes about 2 minutes to run (Ill fix it later I promise)

def printGrid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end='')
        print()

def pad(grid):
    #pad top
    if '#' in grid[0]:
        grid = [['.' for x in range(len(grid[0]))]] + grid
    #pad bottom
    if '#' in grid[-1]:
        grid.append(['.' for x in range(len(grid[0]))])
    #pad left
    if '#' in [grid[y][0] for y in range(len(grid))]:
        for y in range(len(grid)):
            grid[y] = ['.'] + grid[y]
    #pad right
    if '#' in [grid[y][-1] for y in range(len(grid))]:
        for y in range(len(grid)):
            grid[y] += ['.']
    return grid

def propose(grid, y:int, x:int, round:int):
    if '#' not in [grid[y+1][x+1],grid[y+1][x],grid[y+1][x-1],grid[y][x+1],grid[y][x-1],grid[y-1][x+1],grid[y-1][x],grid[y-1][x-1]]:
        return (y, x)
    i = round % 4
    for j in range(4):
        if i == 0:
            if '#' not in [grid[y-1][x+1],grid[y-1][x],grid[y-1][x-1]]:
                return (y-1, x)
        elif i == 1:
            if '#' not in [grid[y+1][x+1],grid[y+1][x],grid[y+1][x-1]]:
                return (y+1, x)
        elif i == 2:
            if '#' not in [grid[y+1][x-1],grid[y][x-1],grid[y-1][x-1]]:
                return (y, x-1)
        else:
            if '#' not in [grid[y+1][x+1],grid[y][x+1],grid[y-1][x+1]]:
                return (y, x+1)
        i = (i+1) % 4
    return (y, x)


def solution():

    #read data
    with open("day23/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    #make grid
    grid = [['' for x in range(len(data[y]))] for y in range(len(data))]
    for y in range(len(data)):
        for x in range(len(data[y])):
            grid[y][x] = data[y][x]

    round = 0
    oldProposals = {}
    while 1:

        #pad the grid
        grid = pad(grid)
    
        #each elf makes a proposal
        proposals = {}
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '#':
                    py, px = propose(grid, y, x, round)
                    proposals[(y, x)] = (py, px)
        
        #execute non-duplicate proposals
        for y, x in proposals.keys():
            proposal = proposals[(y, x)]
            if list(proposals.values()).count(proposal) > 1:
                continue
            py, px = proposal
            grid[y][x] = '.'
            grid[py][px] = '#'

        #check if the proposals have changed since the last round
        if proposals == oldProposals:
            break
        oldProposals = proposals
        round += 1

    return round


print(solution())