
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    data = data[0].split(",")
    
    total = 0
    for s in data:
        x = 0
        for c in s:
            x += ord(c)
            x *= 17
            x %= 256
        total += x

    return total


print(solution())