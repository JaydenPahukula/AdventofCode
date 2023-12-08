
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    path = data[0]

    d = {}
    for line in data[2:]:
        line = line.split()
        d[line[0]] = (line[2][1:-1], line[3][:-1])

    curr = "AAA"
    i = 0
    while 1:
        dir = path[i%len(path)]
        if dir == "L": curr = d[curr][0]
        else: curr = d[curr][1]
        i += 1
        if curr == "ZZZ": break

    return i


print(solution())