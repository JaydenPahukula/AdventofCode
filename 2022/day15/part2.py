

def r(sensor, beacon, row):
    dy = abs(sensor[0]-row)
    d = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
    return range(sensor[1]-(d-dy),sensor[1]+(d-dy))

def getDistance(sensor, coords):
    return abs(sensor[0]-coords[0]) + abs(sensor[1]-coords[1])

def solution():

    with open("day15/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    sensors = {}
    for line in data:
        line = line.split(' ')
        sensors[(int(line[3][2:-1]), int(line[2][2:-1]))] = (int(line[9][2:]), int(line[8][2:-1]))

    ds = {}
    for sensor in sensors:
        beacon = sensors[sensor]
        ds[sensor] = getDistance(sensor, beacon)

    def check(coords):
        for sensor in sensors:
            if getDistance(sensor, coords) < ds[sensor]:
                return False
        return True

    for y in range(4000000):
        for x in range(4000000):
            if check((y, x)):
                return (y, x)
        print(y)


    return

print(solution())


# def check(point, sensors):
#     #print(point, "------")
#     for sensor in sensors:
#         beacon = sensors[sensor]
#         d = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
#         d1 = abs(sensor[0]-point[0]) + abs(sensor[1]-point[1])
#         #print(d, d1)
#         if d1 <= d:
#             return False
#     return True

# def solution():

#     with open("day15/input.txt", "r") as file:
#         data = [x.replace('\n','') for x in file.readlines()]
    
#     sensors = {}
#     for line in data:
#         line = line.split(' ')
#         sensors[(int(line[3][2:-1]), int(line[2][2:-1]))] = (int(line[9][2:]), int(line[8][2:-1]))

#     grid = [[1 for x in range(4000000)] for y in range(4000000)]

#     for y in range(4000000):
#         for x in range(4000000):
#             if check((y, x), sensors):
#                 grid[y][x] = 0
#         print(y)


#     return

# print(solution())