import heapq

def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    grid = [[int(c) for c in line] for line in data]
    h = len(grid)
    w = len(grid[0])

    q = [(0,0,0,"down",0)]
    visited = set()
    while q:
        weight, x, y, direction, dist = heapq.heappop(q)

        if (x,y,direction,dist) in visited: continue
        visited.add((x,y,direction,dist))

        if (x, y) == (w-1, h-1):
            return weight

        if y > 0 and direction != "down" and (direction != "up" or dist < 3):
            heapq.heappush(q, (weight+grid[y-1][x], x, y-1, "up", dist+1 if direction == "up" else 1))
        if y < h-1 and direction != "up" and (direction != "down" or dist < 3):
            heapq.heappush(q, (weight+grid[y+1][x], x, y+1, "down", dist+1 if direction == "down" else 1))
        if x > 0 and direction != "right" and (direction != "left" or dist < 3):
            heapq.heappush(q, (weight+grid[y][x-1], x-1, y, "left", dist+1 if direction == "left" else 1))
        if x < w-1 and direction != "left" and (direction != "right" or dist < 3):
            heapq.heappush(q, (weight+grid[y][x+1], x+1, y, "right", dist+1 if direction == "right" else 1))

    return


print(solution())