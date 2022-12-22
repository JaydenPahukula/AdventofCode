# WARNING: The size and layout of the cube is hardcoded like this:
#
#     +---+---+
#     | 0 | 1 |
#     +---+---+
#     | 2 |
# +---+---+
# | 3 | 4 |
# +---+---+
# | 5 |
# +---+

def move(cube, distance, x, y, side, facing):
    size = len(cube[0])
    for _ in range(distance):

        #set the target coords and parameters, and wrap around if needed
        tx = x
        ty = y
        tside = side
        tfacing = facing
        if tfacing == 0: #facing right
            tx += 1
            if tx >= size:
                if tside == 0:
                    tside = 1
                    tx = 0
                elif tside == 1:
                    tside = 4
                    ty = (size-1)-ty
                    tx = (size-1)
                    tfacing = 2
                elif tside == 2:
                    tside = 1
                    tx = ty
                    ty = (size-1)
                    tfacing = 3
                elif tside == 3:
                    tside = 4
                    tx = 0
                elif tside == 4:
                    tside = 1
                    ty = (size-1)-ty
                    tx = (size-1)
                    tfacing = 2
                else:
                    tside = 4
                    tx = ty
                    ty = (size-1)
                    tfacing = 3
        elif tfacing == 1: #facing down
            ty += 1
            if ty >= size:
                if tside == 0:
                    tside = 2
                    ty = 0
                elif tside == 1:
                    tside = 2
                    ty = tx
                    tx = (size-1)
                    tfacing = 2
                elif tside == 2:
                    tside = 4
                    ty = 0
                elif tside == 3:
                    tside = 5
                    ty = 0
                elif tside == 4:
                    tside = 5
                    ty = tx
                    tx = (size-1)
                    tfacing = 2
                else:
                    tside = 1
                    ty = 0
                    tx = (size-1)-tx
        elif tfacing == 2: #facing left
            tx -= 1
            if tx < 0:
                if tside == 0:
                    tside = 3
                    ty = (size-1)-ty
                    tx = 0
                    tfacing = 0
                elif tside == 1:
                    tside = 0
                    tx = (size-1)
                elif tside == 2:
                    tside = 3
                    tx = ty
                    ty = 0
                    tfacing = 1
                elif tside == 3:
                    tside = 0
                    ty = (size-1)-ty
                    tx = 0
                    tfacing = 0
                elif tside == 4:
                    tside = 3
                    tx = 0
                else:
                    tside = 0
                    tx = ty
                    ty = 0
                    tfacing = 1
        else: #facing up
            ty -= 1
            if ty < 0:
                if tside == 0:
                    tside = 5
                    ty = tx
                    tx = 0
                    tfacing = 0
                elif tside == 1:
                    tside = 5
                    ty = (size-1)
                    tx = (size-1)-tx
                elif tside == 2:
                    tside = 0
                    ty = (size-1)
                elif tside == 3:
                    tside = 2
                    ty = tx
                    tx = 0
                    tfacing = 0
                elif tside == 4:
                    tside = 2
                    ty = (size-1)
                else:
                    tside = 3
                    ty = (size-1)
        
        #check if there is a wall at target coords
        if cube[tside][ty][tx] == '#':
            break
        
        #if not, update coords and parameters
        side, y, x, facing = tside, ty, tx, tfacing

    return (side, y, x, facing)
            

def solution():

    #read data
    with open("day21/input.txt", "r") as file:
        data = [x for x in file.readlines()]
    
    #build cube from data
    size = 50
    cube = [[[' ' for x in range(size)] for y in range(size)] for side in range(6)]
    cubeBuffers = [(0, size), (0, size*2), (size, size), (size*2, 0), (size*2, size), (size*3, 0)]
    for side in range(6):
        for y in range(size):
            for x in range(size):
                cube[side][y][x] = data[y + cubeBuffers[side][0]][x + cubeBuffers[side][1]]

    #follow instructions
    side = 0
    y = 0
    x = cube[side][y].index('.')
    facing = 0
    distance = ""
    for char in data[-1]:
        if char == 'R':
            side, y, x, facing = move(cube, int(distance), x, y, side, facing)
            distance = ""
            facing = (facing+1) % 4
        elif char == 'L':
            side, y, x, facing = move(cube, int(distance), x, y, side, facing)
            distance = ""
            facing = (facing-1) % 4
        else:
            distance += char
    #remainder
    if distance != "":
        side, y, x, facing = move(cube, int(distance), x, y, side, facing) 

    #reformat coords to original layout
    y += cubeBuffers[side][0]
    x += cubeBuffers[side][1]

    return (1000*y) + (4*x) + facing + 1004


print(solution())