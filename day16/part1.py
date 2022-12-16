

def solution():

    with open("day16/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    flowrate = {}
    tunnels = {}
    id = {}
    di = []
    for i, line in enumerate(data):
        valve = line.split(' ')[1]
        flowrate[valve] = int(line.split(';')[0][23:])
        tunnels[valve] = [x[:-1] for x in line.split(' ')[9:-1]]
        tunnels[valve].append(line.split(' ')[-1])
        id[valve] = i
        di.append(valve)
        i += 1

    start = [False for i in range(len(id))]
    for i in range(len(start)):
        if flowrate[di[i]] == 0:
            start[i] = True
    on = {"":start}
    on[""][0] = True
    paths = [("", "AA", 0)]
    numDone = 0
    for min in range(30):
        print("\nminute", min, "=================================")
        print(len(paths), numDone)
        #print(paths)
        l = len(paths)
        for i in range(l):
            (path, curr, score), *paths = paths
            #print("at", path, curr, score, "-------------")

            #add score
            #print(on[path])
            for i, valve in enumerate(on[path]):
                if valve:
                    #print("  +", flowrate[di[i]], "from", di[i])
                    score += flowrate[di[i]]

            #print(on[path])
            if False not in on[path]:
                return
            
            #turn on valve
            if not on[path][id[curr]]:
                paths.append((path+"()", curr, score))
                on[path+"()"] = on[path].copy()
                on[path+"()"][id[curr]] = True
                #print("opening")
            
            #travel somewhere
            #else:
            for tunnel in tunnels[curr]:
                if flowrate[tunnel] > 0:
                    paths.append((path+"->", tunnel, score))
                    on[path+"->"] = on[path].copy()
                    #print("going to", tunnel)
        
        #input()
    
    for path in paths:
        print(path)
        print(on[path[0]])

    return max([x[2] for x in paths])


print(solution())