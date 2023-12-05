
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    rawSeeds = list(map(int, data[0].split()[1:]))
    seeds = []
    for i in range(0, len(rawSeeds), 2):
        seeds.append((rawSeeds[i], rawSeeds[i]+rawSeeds[i+1]))

    lineIndex = 3
    # seed to soil
    newSeeds = []
    done = [False for _ in range(len(seeds))]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, sourceStart, rang = map(int, data[lineIndex].split())
        sourceEnd = sourceStart+rang
        delta = dest-sourceStart
        for i in range(len(seeds)):
            if done[i]: continue
            start, end = seeds[i]
            if start >= sourceStart and start < sourceEnd and end <= sourceEnd and end > sourceStart:
                newSeeds.append((start+delta, end+delta))
                done[i] = True
            elif start >= sourceStart and start < sourceEnd:
                newSeeds.append((start+delta, sourceEnd+delta))
                seeds[i] = (sourceEnd, end)
            elif end <= sourceEnd and end > sourceStart:
                newSeeds.append((sourceStart+delta, end+delta))
                seeds[i] = (start, sourceStart)
        lineIndex += 1
    for i in range(len(seeds)):
        if not done[i]: newSeeds.append(seeds[i])
    seeds = newSeeds
    lineIndex += 2

    # soil to fert
    newSeeds = []
    done = [False for _ in range(len(seeds))]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, sourceStart, rang = map(int, data[lineIndex].split())
        sourceEnd = sourceStart+rang
        delta = dest-sourceStart
        for i in range(len(seeds)):
            if done[i]: continue
            start, end = seeds[i]
            if start >= sourceStart and start < sourceEnd and end <= sourceEnd and end > sourceStart:
                newSeeds.append((start+delta, end+delta))
                done[i] = True
            elif start >= sourceStart and start < sourceEnd:
                newSeeds.append((start+delta, sourceEnd+delta))
                seeds[i] = (sourceEnd, end)
            elif end <= sourceEnd and end > sourceStart:
                newSeeds.append((sourceStart+delta, end+delta))
                seeds[i] = (start, sourceStart)
        lineIndex += 1
    for i in range(len(seeds)):
        if not done[i]: newSeeds.append(seeds[i])
    seeds = newSeeds
    lineIndex += 2

    # fert to water
    newSeeds = []
    done = [False for _ in range(len(seeds))]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, sourceStart, rang = map(int, data[lineIndex].split())
        sourceEnd = sourceStart+rang
        delta = dest-sourceStart
        for i in range(len(seeds)):
            if done[i]: continue
            start, end = seeds[i]
            if start >= sourceStart and start < sourceEnd and end <= sourceEnd and end > sourceStart:
                newSeeds.append((start+delta, end+delta))
                done[i] = True
            elif start >= sourceStart and start < sourceEnd:
                newSeeds.append((start+delta, sourceEnd+delta))
                seeds[i] = (sourceEnd, end)
            elif end <= sourceEnd and end > sourceStart:
                newSeeds.append((sourceStart+delta, end+delta))
                seeds[i] = (start, sourceStart)
        lineIndex += 1
    for i in range(len(seeds)):
        if not done[i]: newSeeds.append(seeds[i])
    seeds = newSeeds
    lineIndex += 2

    # water to light
    newSeeds = []
    done = [False for _ in range(len(seeds))]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, sourceStart, rang = map(int, data[lineIndex].split())
        sourceEnd = sourceStart+rang
        delta = dest-sourceStart
        for i in range(len(seeds)):
            if done[i]: continue
            start, end = seeds[i]
            if start >= sourceStart and start < sourceEnd and end <= sourceEnd and end > sourceStart:
                newSeeds.append((start+delta, end+delta))
                done[i] = True
            elif start >= sourceStart and start < sourceEnd:
                newSeeds.append((start+delta, sourceEnd+delta))
                seeds[i] = (sourceEnd, end)
            elif end <= sourceEnd and end > sourceStart:
                newSeeds.append((sourceStart+delta, end+delta))
                seeds[i] = (start, sourceStart)
        lineIndex += 1
    for i in range(len(seeds)):
        if not done[i]: newSeeds.append(seeds[i])
    seeds = newSeeds
    lineIndex += 2

    # light to temp
    newSeeds = []
    done = [False for _ in range(len(seeds))]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, sourceStart, rang = map(int, data[lineIndex].split())
        sourceEnd = sourceStart+rang
        delta = dest-sourceStart
        for i in range(len(seeds)):
            if done[i]: continue
            start, end = seeds[i]
            if start >= sourceStart and start < sourceEnd and end <= sourceEnd and end > sourceStart:
                newSeeds.append((start+delta, end+delta))
                done[i] = True
            elif start >= sourceStart and start < sourceEnd:
                newSeeds.append((start+delta, sourceEnd+delta))
                seeds[i] = (sourceEnd, end)
            elif end <= sourceEnd and end > sourceStart:
                newSeeds.append((sourceStart+delta, end+delta))
                seeds[i] = (start, sourceStart)
        lineIndex += 1
    for i in range(len(seeds)):
        if not done[i]: newSeeds.append(seeds[i])
    seeds = newSeeds
    lineIndex += 2

    # temp to humid
    newSeeds = []
    done = [False for _ in range(len(seeds))]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, sourceStart, rang = map(int, data[lineIndex].split())
        sourceEnd = sourceStart+rang
        delta = dest-sourceStart
        for i in range(len(seeds)):
            if done[i]: continue
            start, end = seeds[i]
            if start >= sourceStart and start < sourceEnd and end <= sourceEnd and end > sourceStart:
                newSeeds.append((start+delta, end+delta))
                done[i] = True
            elif start >= sourceStart and start < sourceEnd:
                newSeeds.append((start+delta, sourceEnd+delta))
                seeds[i] = (sourceEnd, end)
            elif end <= sourceEnd and end > sourceStart:
                newSeeds.append((sourceStart+delta, end+delta))
                seeds[i] = (start, sourceStart)
        lineIndex += 1
    for i in range(len(seeds)):
        if not done[i]: newSeeds.append(seeds[i])
    seeds = newSeeds
    lineIndex += 2

    # humid to location
    newSeeds = []
    done = [False for _ in range(len(seeds))]
    while lineIndex < len(data) and data[lineIndex] != "":
        dest, sourceStart, rang = map(int, data[lineIndex].split())
        sourceEnd = sourceStart+rang
        delta = dest-sourceStart
        for i in range(len(seeds)):
            if done[i]: continue
            start, end = seeds[i]
            if start >= sourceStart and start < sourceEnd and end <= sourceEnd and end > sourceStart:
                newSeeds.append((start+delta, end+delta))
                done[i] = True
            elif start >= sourceStart and start < sourceEnd:
                newSeeds.append((start+delta, sourceEnd+delta))
                seeds[i] = (sourceEnd, end)
            elif end <= sourceEnd and end > sourceStart:
                newSeeds.append((sourceStart+delta, end+delta))
                seeds[i] = (start, sourceStart)
        lineIndex += 1
    for i in range(len(seeds)):
        if not done[i]: newSeeds.append(seeds[i])
    seeds = newSeeds
    lineIndex += 2
    
    return min(x[0] for x in seeds)


print(solution())