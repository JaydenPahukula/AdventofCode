
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    seeds = list(map(int, data[0].split()[1:]))
    n = len(seeds)
    
    lineIndex = 3
    # seed to soil
    done = [False for _ in range(n)]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, source, rang = map(int, data[lineIndex].split())
        for i in range(n):
            if done[i]: continue
            if seeds[i] >= source and seeds[i] < source+rang:
                seeds[i] += dest-source
                done[i] = True
        lineIndex += 1
    lineIndex += 2
    
    # soil to fert
    done = [False for _ in range(n)]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, source, rang = map(int, data[lineIndex].split())
        for i in range(n):
            if done[i]: continue
            if seeds[i] >= source and seeds[i] < source+rang:
                seeds[i] += dest-source
                done[i] = True
        lineIndex += 1
    lineIndex += 2
    
    # fert to water
    done = [False for _ in range(n)]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, source, rang = map(int, data[lineIndex].split())
        for i in range(n):
            if done[i]: continue
            if seeds[i] >= source and seeds[i] < source+rang:
                seeds[i] += dest-source
                done[i] = True
        lineIndex += 1
    lineIndex += 2
    
    # water to light
    done = [False for _ in range(n)]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, source, rang = map(int, data[lineIndex].split())
        for i in range(n):
            if done[i]: continue
            if seeds[i] >= source and seeds[i] < source+rang:
                seeds[i] += dest-source
                done[i] = True
        lineIndex += 1
    lineIndex += 2
    
    # light to temp
    done = [False for _ in range(n)]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, source, rang = map(int, data[lineIndex].split())
        for i in range(n):
            if done[i]: continue
            if seeds[i] >= source and seeds[i] < source+rang:
                seeds[i] += dest-source
                done[i] = True
        lineIndex += 1
    lineIndex += 2
    
    # temp to humid
    done = [False for _ in range(n)]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, source, rang = map(int, data[lineIndex].split())
        for i in range(n):
            if done[i]: continue
            if seeds[i] >= source and seeds[i] < source+rang:
                seeds[i] += dest-source
                done[i] = True
        lineIndex += 1
    lineIndex += 2
    
    # humid to location
    done = [False for _ in range(n)]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, source, rang = map(int, data[lineIndex].split())
        for i in range(n):
            if done[i]: continue
            if seeds[i] >= source and seeds[i] < source+rang:
                seeds[i] += dest-source
                done[i] = True
        lineIndex += 1
    lineIndex += 2

    return min(seeds)


print(solution())