from collections import deque

def getCount(grid, starting):
    h = len(grid)
    w = len(grid[0])
    q = deque([starting])
    visited = [[[] for _ in range(w)] for _ in range(h)]

    while q:
        l = len(q)
        for _ in range(l):
            x, y, dir = q.popleft()

            if x < 0 or x >= w or y < 0 or y >= h: continue
            if dir in visited[y][x]: continue
            visited[y][x].append(dir)

            tile = grid[y][x]
            if tile == ".":
                if dir == "left": q.append((x-1, y, "left"))
                elif dir == "up": q.append((x, y-1, "up"))
                elif dir == "right": q.append((x+1, y, "right"))
                else: q.append((x, y+1, "down"))
            elif tile == "/":
                if dir == "right": q.append((x, y-1, "up"))
                elif dir == "up": q.append((x+1, y, "right"))
                elif dir == "left": q.append((x, y+1, "down"))
                else: q.append((x-1, y, "left"))
            elif tile == "\\":
                if dir == "left": q.append((x, y-1, "up"))
                elif dir == "up": q.append((x-1, y, "left"))
                elif dir == "right": q.append((x, y+1, "down"))
                else: q.append((x+1, y, "right"))
            elif tile == "|":
                if dir in ("left", "right"):
                    q.append((x, y+1, "down"))
                    q.append((x, y-1, "up"))
                elif dir == "up": q.append((x, y-1, "up"))
                else: q.append((x, y+1, "down"))
            elif tile == "-":
                if dir in ("up", "down"):
                    q.append((x-1, y, "left"))
                    q.append((x+1, y, "right"))
                elif dir == "left": q.append((x-1, y, "left"))
                else: q.append((x+1, y, "right"))

    count = 0
    for y in range(h):
        for x in range(w):
            if visited[y][x]: count += 1
    
    return count


def solution():

    with open("input.txt", "r") as file:
        grid = [x.replace('\n','') for x in file.readlines()]
    
    h = len(grid)
    w = len(grid[0])

    maxCount = 0
    for x in range(w):
        newCount = getCount(grid, (x, 0, "down"))
        if newCount > maxCount: maxCount = newCount
        newCount = getCount(grid, (x, h-1, "up"))
        if newCount > maxCount: maxCount = newCount
    for y in range(h):
        newCount = getCount(grid, (0, y, "right"))
        if newCount > maxCount: maxCount = newCount
        newCount = getCount(grid, (w-1, y, "left"))
        if newCount > maxCount: maxCount = newCount

    return maxCount


print(solution())