

def solution():

    with open("day16/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    flowrate = {}
    tunnels = {}
    id = {}
    for i, line in enumerate(data):
        valve = line.split(' ')[1]
        flowrate[valve] = int(line.split(';')[0][23:])
        tunnels[valve] = [x[:-1] for x in line.split(' ')[9:-1]]
        tunnels[valve].append(line.split(' ')[-1])
        id[valve] = i
        i += 1

    #all valves with flowrate of 0 are considered on
    start = [-1 for i in range(len(flowrate))]
    for i in range(len(start)):
        if flowrate[list(flowrate.keys())[i]] == 0:
            start[i] = 0
    
    #queue
    paths = [("", "AA", start)]

    for min in range(30):
        print("\nminute", min, "=================================")
        print(len(paths))

        l = len(paths)
        for i in range(l):
            #increment queue
            (path, curr, on), *paths = paths

            #if all valves are on
            if -1 not in on:
                paths.append((path, curr, on))
                print("skipping")
                continue
            
            #turn on valve
            if on[id[curr]] == -1:
                newon = on.copy()
                newon[id[curr]] = min
                paths.append((path+curr, curr, newon))
            
            #travel somewhere
            for tunnel in tunnels[curr]:
                paths.append((path+"->", tunnel, on))

        #input()

    return


print(solution())