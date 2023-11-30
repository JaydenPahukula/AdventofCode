
def solution():

    with open("day06/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines() if x != ""][0]
    
    x = list(data[:13])
    i = 14
    for c in data[13:]:
        x.append(c)
        print(x)
        if len(x) == len(set(x)):
            return i
        x.pop(0)
        i += 1


print(solution())