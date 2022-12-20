
def shift(l:list, num:int):
    index = l.index(num)
    #rotate list until num is at the front
    l = [l[(i + index) % len(l)] for i, x in enumerate(l)]
    #remove num
    l.pop(0)
    #insert it back in the middle
    l.insert((int(num) % len(l)), num)
    return l

def solution():

    #read data
    with open("day20/input.txt", "r") as file:
        data = [int(x.replace('\n','')) for x in file.readlines()]
    
    #deal with duplicates
    known = []
    for i in range(len(data)):
        while data[i] in known:
            data[i] += 0.001 * (data[i]/abs(data[i]))
        known.append(data[i])

    #mix the list
    l = data.copy()
    for num in data:
        l = shift(l, num)

    i = l.index(0)
    return int(l[(1000+i)%len(l)]) + int(l[(2000+i)%len(l)]) + int(l[(3000+i)%len(l)])
 

print(solution())
