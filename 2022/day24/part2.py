
def printGrid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(grid[y][x], end='')
        print()
    return

def solution():

    with open("day24/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    h = len(data)
    w = len(data[0])

    base = [[' ' for x in range(w)] for y in range(h)]
    blizzards = []
    for y in range(h):
        for x in range(w):
            if data[y][x] == '#':
                base[y][x] = '#'
            else:
                base[y][x] = '.'
            
            if data[y][x] not in '#.':
                blizzards.append([y, x, data[y][x]])

    dy = {'>':0, 'v':1, '<':0, '^':-1}
    dx = {'>':1, 'v':0, '<':-1, '^':0}

    grid = []
    for state in range(h*w+1):
        grid.append([[base[y][x] for x in range(w)] for y in range(h)])
        for blizzard in blizzards:
            y, x, direction = blizzard
            if grid[state][y][x] == '.':
                grid[state][y][x] = direction
            elif grid[state][y][x] in '>v<^':
                grid[state][y][x] = '2'
            else:
                grid[state][y][x] = str(int(grid[state][y][x])+1)[0]
            
            blizzard[0] += dy[direction]
            if blizzard[0] == h-1: blizzard[0] = 1
            elif blizzard[0] == 0: blizzard[0] = h-2
            blizzard[1] += dx[direction]
            if blizzard[1] == w-1: blizzard[1] = 1
            elif blizzard[1] == 0: blizzard[1] = w-2
        
        #printGrid(grid[state])
        done = False
        for s in range(state):
            if grid[state] == grid[s]:
                grid.pop()
                done = True
                break
        if done: break
    
    print(len(grid),"\n\n")
    q = [(0, 1, 1)]
    end = (h-1, w-2)
    maxScore = 0
    while len(q) > 0:
        (y, x, n), *q = q
        #print(n)
        #print(n, y, x, "======")
        print(len(q), n, maxScore)
        if (y, x) == end:
            return n-1
        
        if n > 20:
            if y+x > maxScore:
                maxScore = y+x
            elif y+x < maxScore/4:
                continue

        state = (n) % len(grid)

        #printGrid(grid[state])
        l = len(q)
        if grid[state][y+1][x] == '.':
            #print("down")
            q.append((y+1, x, n+1))
        if grid[state][y-1][x] == '.':
            #print("up")
            q.append((y-1, x, n+1))
        if grid[state][y][x+1] == '.':
            #print("right")
            q.append((y, x+1, n+1))
        if grid[state][y][x-1] == '.':
            #print("left")
            q.append((y, x-1, n+1))

        if l == len(q):
            q.append((y, x, n+1))


    return "couldn't find solution"


print(solution())