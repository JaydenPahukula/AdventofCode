from collections import deque

def solution():

    with open("input.txt", "r") as file:
        grid = [x.replace('\n','') for x in file.readlines()]
    
    h = len(grid)
    w = len(grid[0])
    
    visited = [[[] for _ in range(w)] for _ in range(h)]

    q = deque([(0,0,"right")])
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


print(solution())