
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    times = list(map(int, data[0].split()[1:]))
    dists = list(map(int, data[1].split()[1:]))
    n = len(times)

    out = 1
    for i in range(n):
        time = times[i]
        dist = dists[i]
        numWays = 0
        for holdTime in range(1,time):
            newDist = (time-holdTime)*(holdTime)
            if newDist > dist: numWays += 1
        out *= numWays


    return out


print(solution())