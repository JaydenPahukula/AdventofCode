
def solution():

    with open("test.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    n = len(data)
    lines = []
    for line in data:
        line = line.replace(",","").split()
        lines.append((int(line[0]),int(line[1]),int(line[2]),int(line[4]),int(line[5]),int(line[6])))
    
    x1,y1,z1,vx1,vy1,vz1 = lines[0]
    x2,y2,z2,vx2,vy2,vz2 = lines[1]
    x3,y3,z3,vx3,vy3,vz3 = lines[2]

    def dot(t:float):
        xa,ya,za = x1+vx1*t, y1+vy1*t, z1+vz1*t
        xb,yb,zb = x2+vx2*t, y2+vy2*t, z2+vz2*t
        xc,yc,zc = x3+vx3*t, y3+vy3*t, z3+vz3*t
        xab,yab,zab = xa-xb, ya-yb, za-zb
        xbc,ybc,zbc = xb-xc, yb-yc, zb-zc
        # print(xa,ya,za,xb,yb,zb,xc,yc,zc)
        return xab*xbc + yab*ybc + zab*zbc

    lo = -10**3
    hi = 10**3
    while hi-lo > 0.0001:
        m1 = lo+(hi-lo)/3
        m2 = lo+2*(hi-lo)/3
        result1 = dot(m1)
        result2 = dot(m2)
        print(lo, result1, result2, hi)
        if result1 > result2:
            hi = m2
        else:
            lo = m1

    return lo, hi


print(solution())