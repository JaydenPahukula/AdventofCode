
def area(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area


def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    instructions = []
    d = "RDLU"
    for line in data:
        _, _, color = line.split()
        direction = d[int(color[-2])]
        amount = int(color[2:-2], 16)
        instructions.append((direction, amount))
    
    x,y = 0, 0
    coords = []
    borderCount = 0
    for direction, amount in instructions:
        amount = int(amount)
        borderCount += amount
        if direction == "U":
            y -= amount
        elif direction == "D":
            y += amount
        elif direction == "R":
            x -= amount
        else:
            x += amount
        coords.append((x,y))
    
    return int(area(coords)) + (borderCount//2) + 1


print(solution())


# import heapq

# def solution():

#     with open("test.txt", "r") as file:
#         data = [x.replace('\n','') for x in file.readlines()]

#     instructions = []
#     d = "RDLU"
#     for line in data:
#         _, _, color = line.split()
#         direction = d[int(color[-2])]
#         amount = int(color[2:-2], 16)
#         instructions.append((direction, amount))
    
#     h = w = 10**7
#     rows = [[] for _ in range(h)]
    
#     x,y = w//2, h//2
#     heapq.heappush(rows[y], x)
#     for direction, amount in instructions:
#         if direction == "U":
#             heapq.heappush(rows[y], x)
#             for _ in range(amount):
#                 y -= 1
#                 heapq.heappush(rows[y], x)
#         elif direction == "D":
#             heapq.heappush(rows[y], x)
#             for _ in range(amount):
#                 y += 1
#                 heapq.heappush(rows[y], x)
#         # elif direction == "R":
#         #     for _ in range(amount):
#         #         x -= 1
#         #         heapq.heappush(rows[y], x)
#         # else:
#         #     for _ in range(amount):
#         #         x += 1
#         #         heapq.heappush(rows[y], x)

#     count = 0
#     for y in range(h-1):
#         last = -1
#         while rows[y]:
#             x = heapq.heappop(rows[y])
#             if last == -1:
#                 last = x
#             else:
#                 count += x-last+1
#                 last = -1
#         if last != -1:print(cp[y])

#     return count


# print(solution())



# 92555779108903 too low
# 92556687099370 too low
# 952406975581
# 952406718538