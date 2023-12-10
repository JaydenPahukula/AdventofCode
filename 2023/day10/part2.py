
def solution():

    with open("input.txt", "r") as file:
        grid = [x.replace('\n','') for x in file.readlines()]
    newGrid = [["." for c in line] for line in grid]
    
    h = len(grid)
    w = len(grid[0])
    Sy, Sx = 0, 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "S":
                Sy, Sx = y, x

    ay, ax = Sy, Sx
    by, bx = Sy, Sx
    aFrom = bFrom = ""
    
    if Sy > 0 and grid[Sy-1][Sx] in "|7F": ay, ax = Sy-1, Sx; aFrom = "down"
    elif Sx < w-1 and grid[Sy][Sx+1] in "-7J": ay, ax = Sy, Sx+1; aFrom = "left"
    elif Sy < h-1 and grid[Sy+1][Sx] in "|LJ": ay, ax = Sy+1, Sx; aFrom = "up"
    elif Sx > 0 and grid[Sy][Sx-1] in "-LF": ay, ax = Sy, Sx-1; aFrom = "right"

    if Sx > 0 and grid[Sy][Sx-1] in "-LF": by, bx = Sy, Sx-1; bFrom = "right"
    elif Sy < h-1 and grid[Sy+1][Sx] in "|LJ": by, bx = Sy+1, Sx; bFrom = "up"
    elif Sx < w-1 and grid[Sy][Sx+1] in "-7J": by, bx = Sy, Sx+1; bFrom = "left"
    elif Sy > 0 and grid[Sy-1][Sx] in "|7F": by, bx = Sy-1, Sx; bFrom = "down"

    steps = 1
    while 1:

        newGrid[ay][ax] = grid[ay][ax]
        newGrid[by][bx] = grid[by][bx]

        if aFrom == "up":
            if grid[ay][ax] == "J":ay, ax = ay, ax-1; aFrom = "right"
            elif grid[ay][ax] == "|":ay, ax = ay+1, ax; aFrom = "up"
            elif grid[ay][ax] == "L":ay, ax = ay, ax+1; aFrom = "left"
        elif aFrom == "down":
            if grid[ay][ax] == "7":ay, ax = ay, ax-1; aFrom = "right"
            elif grid[ay][ax] == "|":ay, ax = ay-1, ax; aFrom = "down"
            elif grid[ay][ax] == "F":ay, ax = ay, ax+1; aFrom = "left"
        elif aFrom == "left":
            if grid[ay][ax] == "J":ay, ax = ay-1, ax; aFrom = "down"
            elif grid[ay][ax] == "-":ay, ax = ay, ax+1; aFrom = "left"
            elif grid[ay][ax] == "7":ay, ax = ay+1, ax; aFrom = "up"
        elif aFrom == "right":
            if grid[ay][ax] == "L":ay, ax = ay-1, ax; aFrom = "down"
            elif grid[ay][ax] == "-":ay, ax = ay, ax-1; aFrom = "right"
            elif grid[ay][ax] == "F":ay, ax = ay+1, ax; aFrom = "up"

        if bFrom == "up":
            if grid[by][bx] == "J":by, bx = by, bx-1; bFrom = "right"
            elif grid[by][bx] == "|":by, bx = by+1, bx; bFrom = "up"
            elif grid[by][bx] == "L":by, bx = by, bx+1; bFrom = "left"
        elif bFrom == "down":
            if grid[by][bx] == "7":by, bx = by, bx-1; bFrom = "right"
            elif grid[by][bx] == "|":by, bx = by-1, bx; bFrom = "down"
            elif grid[by][bx] == "F":by, bx = by, bx+1; bFrom = "left"
        elif bFrom == "left":
            if grid[by][bx] == "J":by, bx = by-1, bx; bFrom = "down"
            elif grid[by][bx] == "-":by, bx = by, bx+1; bFrom = "left"
            elif grid[by][bx] == "7":by, bx = by+1, bx; bFrom = "up"
        elif bFrom == "right":
            if grid[by][bx] == "L":by, bx = by-1, bx; bFrom = "down"
            elif grid[by][bx] == "-":by, bx = by, bx-1; bFrom = "right"
            elif grid[by][bx] == "F":by, bx = by+1, bx; bFrom = "up"
        
        steps += 1
        if (ay, ax) == (by, bx): break

    newGrid[ay][ax] = grid[ay][ax]
    for line in newGrid:
        print("".join(line))

    return steps


print(solution())