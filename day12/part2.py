
def solution():

    with open("day12/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    h = len(data)
    w = len(data[0])

    #read heightmap
    height = []
    for y in range(h):
        row = []
        for x in range(w):
            if data[y][x] == 'S':
                row.append(0)
            elif data[y][x] == 'E':
                row.append(25)
                end = (y, x)
            else:
                row.append(ord(data[y][x])-ord('a'))
        height.append(row)

    #check each a as starting
    min = w*h
    for y1 in range(h):
        for x1 in range(w):
            if data[y1][x1] not in ['a', 'S']:
                continue

            start = (y1, x1)

            q = [start]
            visited = set()
            tb = {}
            while len(q) > 0:
                (y,x), *q = q

                #exit condition
                if (y, x) == end:
                    break

                #check if already visited
                if (y, x) in visited:
                    continue
                
                #add valid adjacent squares
                currHeight = height[y][x]
                if y < h-1 and height[y+1][x] <= currHeight+1 and (y+1, x) not in visited:
                    q.append((y+1, x))
                    tb[(y+1,x)] = (y,x)
                if y > 0 and height[y-1][x] <= currHeight+1 and (y-1, x) not in visited:
                    q.append((y-1, x))
                    tb[(y-1,x)] = (y,x)
                if x < w-1 and height[y][x+1] <= currHeight+1 and (y,x+1) not in visited:
                    q.append((y, x+1))
                    tb[(y,x+1)] = (y,x)
                if x > 0 and height[y][x-1] <= currHeight+1 and (y, x-1) not in visited:
                    q.append((y, x-1))
                    tb[(y,x-1)] = (y,x)

                visited.add((y,x))

            #if failed
            if len(q) == 0:
                continue
            
            #traceback
            curr = end
            path = []
            while curr != start:
                path.append(curr)
                curr = tb[curr]
            
            #check if new minimum
            if len(path) < min:
                min = len(path)

    return min


print(solution())