
def blocking(x, y, data):
        h = data[y][x]
        left = 0
        right = 0
        up = 0
        down = 0
        for x1 in range(x-1,-1,-1):
            left += 1
            if data[y][x1] >= h:
                break
        for x1 in range(x+1,len(data[0])):
            right += 1
            if data[y][x1] >= h:
                break
        for y1 in range(y-1,-1,-1):
            up += 1
            if data[y1][x] >= h:
                break
        for y1 in range(y+1,len(data[0])):
            down += 1
            if data[y1][x] >= h:
                break
        
        left = max([1,left])
        right = max([1,right])
        up = max([1,up])
        down = max([1,down])
        
        return left*right*up*down

def solution():

    with open("day8/input.txt", "r") as file:
        data = [[int(x) for x in line.replace('\n','')] for line in file.readlines()]
    
    maks = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            b = blocking(x, y, data)
            if b > maks:
                maks = b

    return maks


print(solution())