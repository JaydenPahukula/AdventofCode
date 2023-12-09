
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    out = 0
    for line in data:
        line = list(map(int, line.split()))

        lasts = [line[-1]]
        while len(set(line)) > 1:
            newline = [line[i]-line[i-1] for i in range(1,len(line))]
            line = newline
            lasts.append(line[-1])
        
        back = 0
        for x in lasts[::-1]:
            back = back+x

        out += back

    return out


print(solution())