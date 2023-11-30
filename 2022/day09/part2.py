
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

    with open("day09/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines() if x != ""]
    
    directions = [x.split(" ")[0] for x in data]
    lengths = [int(x.split(" ")[1]) for x in data]

    (headx, heady) = 0, 0
    t1 = (0, 0)
    t2 = (0, 0)
    t3 = (0, 0)
    t4 = (0, 0)
    t5 = (0, 0)
    t6 = (0, 0)
    t7 = (0, 0)
    t8 = (0, 0)
    t9 = (0, 0)
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
            
            #move tails
            t1 = moveTail(headx, heady, t1[0], t1[1])
            t2 = moveTail(t1[0], t1[1], t2[0], t2[1])
            t3 = moveTail(t2[0], t2[1], t3[0], t3[1])
            t4 = moveTail(t3[0], t3[1], t4[0], t4[1])
            t5 = moveTail(t4[0], t4[1], t5[0], t5[1])
            t6 = moveTail(t5[0], t5[1], t6[0], t6[1])
            t7 = moveTail(t6[0], t6[1], t7[0], t7[1])
            t8 = moveTail(t7[0], t7[1], t8[0], t8[1])
            t9 = moveTail(t8[0], t8[1], t9[0], t9[1])
            
            #check if already visited
            if (t9[0], t9[1]) not in visited:
                visited.append((t9[0], t9[1]))

    return len(visited)


print(solution())