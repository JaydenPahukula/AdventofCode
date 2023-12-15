
def hash(s):
    x = 0
    for c in s:
        x += ord(c)
        x *= 17
        x %= 256
    return x


def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    data = data[0].split(",")

    lenses = [[] for _ in range(256)]
    for s in data:
        if s[-1] == "-":
            h = hash(s[:-1])
            for i in range(len(lenses[h])):
                if lenses[h][i][0] == s[:-1]:
                    lenses[h].pop(i)
                    break
        else:
            s, n = s.split("=")
            h = hash(s)
            for i in range(len(lenses[h])):
                if lenses[h][i][0] == s:
                    lenses[h][i] = (s, int(n))
                    break
            else:
                lenses[h].append((s, int(n)))
    
    total = 0
    for h in range(256):
        for i in range(len(lenses[h])):
            _, n = lenses[h][i]
            total += (h+1) * (i+1) * n
    
    return total


print(solution())