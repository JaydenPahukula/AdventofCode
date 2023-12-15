
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    grid = []
    grids = []
    for line in data:
        if line == "":
            grids.append(grid)
            grid = []
        else:
            grid.append(line)
    grids.append(grid)

    total = 0
    for grid in grids:

        h = len(grid)
        w = len(grid[0])

        # check vertical
        for x in range(1, w):
            for y in range(h):
                for dx in range(w//2):
                    if x-dx-1 < 0 or x+dx >= w: continue
                    if grid[y][x-dx-1] != grid[y][x+dx]: break
                else: continue
                break
            else:
                total += x
                break
        else:
        
            # check horizontal
            for y in range(1, h):
                for x in range(w):
                    for dy in range(h//2):
                        if y-dy-1 < 0 or y+dy >= h: continue
                        if grid[y-dy-1][x] != grid[y+dy][x]: break
                    else: continue
                    break
                else:
                    total += 100*y
                    break 
                
    return total


print(solution())