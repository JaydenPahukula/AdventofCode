
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    bricks = []
    for line in data:
        a,b = line.split("~")
        ax,ay,az = map(int, a.split(","))
        bx,by,bz = map(int, b.split(","))
        if ax > bx: ax,bx=bx,ax
        if ay > by: ay,by=by,ay
        if az > bz: az,bz=bz,az
        bricks.append([ax,ay,az,bx,by,bz,[],0])
    
    bricks.sort(key=lambda x: x[2])

    for i in range(len(bricks)):
        while bricks[i][2] > 1:
            for j in range(len(bricks)):
                if i == j: continue
                if bricks[i][0] > bricks[j][3] or bricks[i][3] < bricks[j][0]: continue
                if bricks[i][1] > bricks[j][4] or bricks[i][4] < bricks[j][1]: continue
                if bricks[j][5] != bricks[i][2]-1: continue
                
                bricks[j][6].append(i)
                bricks[i][7] += 1
            
            if bricks[i][7] != 0: break

            bricks[i][2] -= 1
            bricks[i][5] -= 1
    
    count = 0
    for brick in bricks:
        for other in brick[6]:
            if bricks[other][7] == 1: break
        else: count += 1

    return count


print(solution())