
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    out = 0
    for line in data:
        line = line.split()
        winning = list(map(int, line[2:12]))
        numWinning = sum([1 if int(x) in winning else 0 for x in line[13:]])
        if numWinning: out += 2**(numWinning-1)

    return out


print(solution())