
def solution():

    with open("day10/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines() if x != ""]
    
    x = 1
    line = 0
    wait = False
    cycle = 1
    score = 0

    while 1:
        
        if not wait:
            command = data[line].split(' ')[0]
            if command == "addx":
                v = int(data[line].split(' ')[1])
                wait = True
            line += 1
            if line == len(data):
                break
        else:
            x += v
            wait = False

        cycle += 1
        if cycle % 40 == 20:
            score += cycle * x

    return score


print(solution())

#13660