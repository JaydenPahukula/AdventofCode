
def solution():

    with open("input.txt", "r") as file:
        grid = [x.replace('\n','') for x in file.readlines()]
    
    h = len(grid)
    w = len(grid[0])
    horizontals = [0 for _ in range(h)]
    verticals = [0 for _ in range(w)]
    for y in range(1, h):
        horizontals[y] = horizontals[y-1]
        if "#" not in grid[y]:
            horizontals[y] += 10**6-1
    for x in range(1, w):
        verticals[x] = verticals[x-1]
        if "#" not in [grid[y][x] for y in range(h)]:
            verticals[x] += 10**6-1
    
    galaxies = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "#":
                galaxies.append((x,y))
    
    total = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            x1, y1 = galaxies[i]
            x2, y2 = galaxies[j]
            total += abs((x1+verticals[x1])-(x2+verticals[x2])) + abs((y1+horizontals[y1])-(y2+horizontals[y2]))

    return total


print(solution())