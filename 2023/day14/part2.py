
def solution():

    with open("input.txt", "r") as file:
        grid = [list(x.replace('\n','')) for x in file.readlines()]

    h = len(grid)
    w = len(grid[0])

    pastGrids = []
    iteration = 0
    while iteration < 1000000000:
        pastGrids.append([line.copy() for line in grid])
        # up
        for y in range(1, h):
            for x in range(w):
                if grid[y][x] == "O":
                    y1 = y-1
                    while y1 >= 0 and grid[y1][x] == ".":
                        grid[y1][x] = "O"
                        grid[y1+1][x] = "."
                        y1 -= 1
        # left
        for x in range(1, w):
            for y in range(h):
                if grid[y][x] == "O":
                    x1 = x-1
                    while x1 >= 0 and grid[y][x1] == ".":
                        grid[y][x1] = "O"
                        grid[y][x1+1] = "."
                        x1 -= 1
        # down
        for y in range(h-2, -1, -1):
            for x in range(w):
                if grid[y][x] == "O":
                    y1 = y+1
                    while y1 <= h-1 and grid[y1][x] == ".":
                        grid[y1][x] = "O"
                        grid[y1-1][x] = "."
                        y1 += 1
        # right
        for x in range(w-2, -1, -1):
            for y in range(h):
                if grid[y][x] == "O":
                    x1 = x+1
                    while x1 <= w-1 and grid[y][x1] == ".":
                        grid[y][x1] = "O"
                        grid[y][x1-1] = "."
                        x1 += 1
        
        for i in range(len(pastGrids)):
            for y in range(h):
                for x in range(w):
                    if pastGrids[i][y][x] != grid[y][x]: break
                else: continue
                break
            else:
                cycle = iteration-i+1
                iteration += ((1000000000-iteration)//cycle)*cycle
                break

        iteration += 1

    total = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "O": total += h-y

    return total


print(solution())