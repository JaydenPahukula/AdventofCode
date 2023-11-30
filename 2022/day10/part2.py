
def solution():

    with open("day10/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines() if x != ""]
    
    x = 1
    line = 0
    wait = False
    cycle = 0
    screen = ['.'] * (40 * 6)

    while 1:

        if abs(cycle%40 - x) <= 1:
            screen[cycle] = '#'

        if not wait:
            command = data[line].split(' ')[0]
            if command == "addx":
                v = int(data[line].split(' ')[1])
                wait = True
            line += 1
            if line == len(data):
                break
        else:
            wait = False
            x += v

        cycle += 1

    #print screen
    for y in range(6):
        for x in range(40):
            print(screen[y*40+x], end='')
        print()

    return


solution()