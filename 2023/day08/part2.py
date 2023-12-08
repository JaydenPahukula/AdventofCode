import math
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    path = data[0]

    d = {}
    curr = []
    for line in data[2:]:
        line = line.split()
        d[line[0]] = (line[2][1:-1], line[3][:-1])
        if line[0][-1] == "A":
            curr.append(line[0])

    for cur in curr:
        print(cur)
        i = 0
        while 1:
            dir = path[i%len(path)]
            if dir == "L":
                cur = d[cur][0]
            else:
                cur = d[cur][1]
            if cur[-1] == "Z":
                print(i, cur)

            i += 1
            if i > 100000: break

    return i


# run this to find cycle lengths
# print(solution())

# solution
print(math.lcm(21883, 19667, 14681, 16897, 13019, 11911))