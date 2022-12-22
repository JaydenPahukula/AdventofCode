
def move(grid, distance, x, y, facing):
    for _ in range(distance):

        #set the target coords and wrap around if need
        tx = x
        ty = y
        if facing == 0: #facing right
            tx += 1
            if tx >= len(grid[ty]) or grid[ty][tx] == ' ':
                tx = 0
                while grid[ty][tx] == ' ':
                    tx += 1
        elif facing == 1: #facing down
            ty += 1
            if ty >= len(grid) or grid[ty][tx] == ' ':
                ty = 0
                while grid[ty][tx] == ' ':
                    ty += 1
        elif facing == 2: #facing left
            tx -= 1
            if tx < 0 or grid[ty][tx] == ' ':
                tx = len(grid[ty])-1
                while grid[ty][tx] == ' ':
                    tx -= 1
        else: #facing up
            ty -= 1
            if ty < 0 or grid[ty][tx] == ' ':
                ty = len(grid)-1
                while grid[ty][tx] == ' ':
                    ty -= 1
        
        #check if there is a wall at target coords
        if grid[ty][tx] == '#':
            break
        
        #if not, update x and y
        y, x = ty, tx

    return (y, x)
            

def solution():

    #read data
    with open("day21/input.txt", "r") as file:
        data = [x for x in file.readlines()]
    
    #build grid from data
    w = max([len(line) for line in data[:-2]])-1
    h = len(data)-2
    grid = [[' ' for x in range(w)] for y in range(h)]
    for y in range(h):
        for x in range(w):
            if data[y][x] == ' ':
                pass
            elif data[y][x] == '.':
                grid[y][x] = '.'
            elif data[y][x] == '#':
                grid[y][x] = '#'
            else:
                break

    #follow instructions
    y = 0
    x = grid[y].index('.')
    facing = 0
    distance = ""
    for char in data[-1]:
        if char == 'R':
            y, x = move(grid, int(distance), x, y, facing)
            distance = ""
            facing = (facing+1) % 4
        elif char == 'L':
            y, x = move(grid, int(distance), x, y, facing)
            distance = ""
            facing = (facing-1) % 4
        else:
            distance += char
    #remainder
    if distance != "":
        y, x = move(grid, int(distance), x, y, facing) 

    return (1000*y) + (4*x) + facing + 1004


print(solution())