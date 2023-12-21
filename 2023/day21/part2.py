
def solution():

    with open("test.txt", "r") as file:
        grid = [x.replace('\n','') for x in file.readlines()]

    h = len(grid)
    w = len(grid[0])
    startx, starty = 0,0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "S":
                startx, starty = x, y

    spaceTime = [[set() for x in range(w)] for y in range(h)]
    spaceTime[starty][startx].add((0,0))
    for i in range(1000):
        newSpaceTime = [[set() for x in range(w)] for y in range(h)]
        # for line in spaceTime:
        #     print(" ".join(str(len(x)) for x in line))
        #input()
        for y in range(h):
            for x in range(w):
                if spaceTime[y][x]:
                    for x1,y1 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                        if grid[y1%h][x1%w] == "#": continue
                        if y1 < 0:
                            for px,py in spaceTime[y][x]:
                                # spaceTime[y][x].remove((px,py))
                                newSpaceTime[y1%h][x1%w].add((px,py-1))
                        elif y1 >= h:
                            for px,py in spaceTime[y][x]:
                                # spaceTime[y][x].remove((px,py))
                                newSpaceTime[y1%h][x1%w].add((px,py+1))
                        elif x1 < 0:
                            for px,py in spaceTime[y][x]:
                                # spaceTime[y][x].remove((px,py))
                                newSpaceTime[y1%h][x1%w].add((px-1,py))
                        elif x1 >= w:
                            for px,py in spaceTime[y][x]:
                                # spaceTime[y][x].remove((px,py))
                                newSpaceTime[y1%h][x1%w].add((px+1,py))
                        else:
                            newSpaceTime[y1][x1] |= spaceTime[y][x]
        spaceTime = newSpaceTime
    
    return sum([sum([len(spaceTime[y][x]) for x in range(w)]) for y in range(h)])


print(solution())