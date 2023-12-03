
NUMS = "0123456789"
def solution():

    with open("input.txt", "r") as file:
        data = [list(x.replace('\n','')) for x in file.readlines()]
    
    total = 0
    h = len(data)
    w = len(data[0])
    for y in range(h):
        for x in range(w):
            if data[y][x] != "." and data[y][x] not in NUMS:
                for y1 in range(max(0, y-1), min(h,y+2)):
                    for x1 in range(max(0, x-1), min(w,x+2)):
                        if (y1,x1) == (y,x): continue
                        if data[y1][x1] not in NUMS: continue
                        start = end = x1
                        while start > 0 and data[y1][start-1] in NUMS: start -= 1
                        while end < w-1 and data[y1][end+1] in NUMS: end += 1
                        num = int("".join(data[y1][start:end+1]))
                        total += num
                        for x2 in range(start,end+1):
                            data[y1][x2] = "."
                        
    return total


print(solution())