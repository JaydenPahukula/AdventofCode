
def solution():

    with open("input.txt", "r") as file:
        grid = [list(x.replace('\n','')) for x in file.readlines()]

    h = len(grid)
    w = len(grid[0])

    for y in range(1, h):
        for x in range(w):
            if grid[y][x] == "O":
                y1 = y-1
                while y1 >= 0 and grid[y1][x] == ".":
                    grid[y1][x] = "O"
                    grid[y1+1][x] = "."
                    y1 -= 1
    
    total = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "O": total += h-y

    return total


print(solution())