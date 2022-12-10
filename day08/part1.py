
def isVisible(x, y, data):
        if x == 0 or x == len(data[0])-1: return False
        if y == 0 or y == len(data)-1: return False
        h = data[y][x]
        for x1 in range(0,x):
            if data[y][x1] >= h:
                break
        else:
            return False
        for x1 in range(x+1,len(data[0])):
            if data[y][x1] >= h:
                break
        else:
            return False
        for y1 in range(0,y):
            if data[y1][x] >= h:
                break
        else:
            return False
        for y1 in range(y+1,len(data[0])):
            if data[y1][x] >= h:
                break
        else:
            return False
        return True

def solution():

    with open("day8/input.txt", "r") as file:
        data = [[int(x) for x in line.replace('\n','')] for line in file.readlines()]

    count = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if not isVisible(x, y, data):
                count += 1

    return count


print(solution())