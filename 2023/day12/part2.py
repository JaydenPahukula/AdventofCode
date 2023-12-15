
def solution():

    with open("test.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    total = 0
    for line in data:
        s, l = line.split()
        s = [x for x in s.split(".") if x]
        l = list(map(int, l.split(",")))
        total += getNums(s, l)
        

    return total


print(solution())

p2=0
for line in open('real.in').readlines():
    s,k = line.strip().split()
    r = [*map(int,k.split(','))]

    s = '?'.join([s]*5)
    r*=5

    def rec(i,j,d={}):
        if (i,j) in d:return d[i,j]
        if i >= len(s) and j == len(r):
            return 1
        if i >= len(s):
            return 0
        if j == len(r):
            return s[i:].count('#') == 0
        
        t = 0
        for k in range(i,len(s)-r[j]+1):
            if s[k:k+r[j]].count('.') == 0 and (k+r[j] == len(s) or s[k+r[j]] != '#'):
                t += rec(k+r[j]+1,j+1)
            if s[k] == '#': break
        d[i,j] = t
        return t
    p2 += rec(0,0)