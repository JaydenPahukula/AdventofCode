
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    h = w = 1000
    grid = [["." for _ in range(w)] for _ in range(h)]
    
    x,y = w//2, h//2
    grid[y][x] = "#"
    for line in data:
        direction, amount, color = line.split()
        if direction == "U":
            for _ in range(int(amount)):
                y -= 1
        elif direction == "D":
            for _ in range(int(amount)):
                y += 1
        elif direction == "R":
            for _ in range(int(amount)):
                x -= 1
        else:
            for _ in range(int(amount)):
                x += 1
        grid[y][x] = "#"

    count = 0
    for y in range(h-1):
        inside = False
        for x in range(w):
            if grid[y][x] == "#" or inside:
                count += 1
            if grid[y-1][x] == "#" and grid[y][x] == "#":
                inside = not inside

    return count


print(solution())