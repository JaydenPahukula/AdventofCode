
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    time = int("".join(data[0].split()[1:]))
    dist = int("".join(data[1].split()[1:]))
    
    numWays = 0
    for holdTime in range(1,time):
        newDist = (time-holdTime)*(holdTime)
        if newDist > dist: numWays += 1

    return numWays


print(solution())