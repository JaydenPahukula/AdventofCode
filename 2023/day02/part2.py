
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    out = 0
    for line in data:
        d = {"red":0, "green":0, "blue":0}
        line = line.split()
        for i in range(2, len(line), 2):
            num = int(line[i])
            color = line[i+1].strip(",").strip(";")
            d[color] = max(d[color], num)
        out += d["red"]*d["green"]*d["blue"]

    return out


print(solution())