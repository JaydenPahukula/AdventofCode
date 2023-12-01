
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    out = 0
    for line in data:
        num = 0
        for c in line:
            if c in "0123456789":
                num += 10*int(c)
                break
        for c in line[::-1]:
            if c in "0123456789":
                num += int(c)
                break
        out += num
    
    return out


print(solution())