
def moveTail(headx, heady, tailx, taily):
    
    #if already adjacent
    if abs(headx-tailx) <= 1 and abs(heady-taily) <= 1:
        pass
    #if directly to the side
    elif abs(headx-tailx) == 0:
        if heady > taily: taily += 1
        else: taily -= 1
    #if directly above/below
    elif abs(heady-taily) == 0:
        if headx > tailx: tailx += 1
        else: tailx -= 1
    #if diagonal
    else:
        if headx > tailx: tailx += 1
        else: tailx -= 1
        if heady > taily: taily += 1
        else: taily -= 1
    
    return (tailx, taily)


def solution():

    with open("day9/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines() if x != ""]
    
    directions = [x.split(" ")[0] for x in data]
    lengths = [int(x.split(" ")[1]) for x in data]

    (headx, heady) = 0, 0
    (tailx, taily) = 0, 0
    visited = []

    for i in range(len(data)):
        direction = directions[i]
        for j in range(lengths[i]):
            #move head
            if direction == 'R':
                headx += 1
            elif direction == 'L':
                headx -= 1
            elif direction == 'U':
                heady += 1
            else:
                heady -= 1
            
            #move tail
            (tailx, taily) = moveTail(headx, heady, tailx, taily)

            #check if already visited
            if (tailx, taily) not in visited:
                visited.append((tailx, taily))

    return len(visited)


print(solution())