
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    out = 0
    for line in data:
        line = line.split()
        id = int(line[1][:-1])
        for i in range(2, len(line), 2):
            num = int(line[i])
            color = line[i+1].strip(",").strip(";")
            if color == "red" and num > 12: break
            if color == "green" and num > 13: break
            if color == "blue" and num > 14: break
        else:
            out += id

    return out


print(solution())