
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    n = len(data)
    lines = []
    for line in data:
        line = line.replace(",","").split()
        lines.append((int(line[0]),int(line[1]),int(line[4]),int(line[5])))

    def inBounds(x:int):
        # return x >= 7 and x <= 27
        return x >= 200000000000000 and x <= 400000000000000
    
    total = 0
    for i in range(n):
        x1,y1,vx1,vy1 = lines[i]
        m1 = vy1/vx1
        b1 = y1-m1*x1
        for j in range(i+1, n):
            x2,y2,vx2,vy2 = lines[j]
            m2 = vy2/vx2
            b2 = y2-m2*x2

            # if parallel
            if m1 == m2:
                continue
            
            # if out of bounds
            intersectX = (b2-b1)/(m1-m2)
            intersectY = m1*intersectX+b1
            if not inBounds(intersectX) or not inBounds(intersectY):
                continue
                
            # if collision in the past
            if (vx1 > 0 and intersectX < x1) or (vx1 < 0 and intersectX > x1):
                continue
            if (vx2 > 0 and intersectX < x2) or (vx2 < 0 and intersectX > x2):
                continue

            # success
            total += 1

    return total


print(solution())