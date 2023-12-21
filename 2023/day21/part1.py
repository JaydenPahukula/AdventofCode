from collections import deque

def solution():

    with open("input.txt", "r") as file:
        grid = [x.replace('\n','') for x in file.readlines()]

    h = len(grid)
    w = len(grid[0])
    startx, starty = 0,0
    valid = set()
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "S":
                startx, starty = x, y
            if grid[y][x] != "#":
                valid.add((x,y))

    q = deque([(startx, starty)])
    queued = set([(startx, starty)])
    for _ in range(64):
        l = len(q)
        for _ in range(l):
            x,y = q.popleft()
            queued.remove((x,y))

            for neighbor in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if neighbor in valid and neighbor not in queued:
                    q.append(neighbor)
                    queued.add(neighbor)

    return len(q)


print(solution())