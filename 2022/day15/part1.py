
def r(sensor, beacon, row):
    dy = abs(sensor[0]-row)
    d = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
    print(d)
    return range(sensor[1]-(d-dy),sensor[1]+(d-dy))

def solution():

    with open("day15/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    sensors = {}
    for line in data:
        line = line.split(' ')
        sensors[(int(line[3][2:-1]), int(line[2][2:-1]))] = (int(line[9][2:]), int(line[8][2:-1]))

    ROW = 2000000
    known = set()
    for sensor in sensors:
        beacon = sensors[sensor]
        #print(sensor, beacon)
        for num in r(sensor, beacon, ROW):
            #print(num)
            known.add(num)


    return len(known)


print(solution())

#8873459 too high
#8473479
# --
#4873479 too low