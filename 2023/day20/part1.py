from collections import deque

def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    moduleType = {}
    adjacent = {}
    for line in data:
        if line[:11] == "broadcaster":
            adjacent["broadcaster"] = line[15:].split(", ")
        else:
            line = line.split(" -> ")
            name, type = line[0][1:], line[0][0]
            moduleType[name] = type
            adjacent[name] = line[1].split(", ")
            for neighbor in adjacent[name]:
                if neighbor not in moduleType: moduleType[neighbor] = ""
                if neighbor not in adjacent: adjacent[neighbor] = []
    
    # initialize states
    moduleState = {}
    for name in moduleType:
        if moduleType[name] == "%": moduleState[name] = False
        elif moduleType[name] == "&": moduleState[name] = (set(),set())
    for name in moduleType:
        for neighbor in adjacent[name]:
            if moduleType[neighbor] == "&": moduleState[neighbor][0].add(name)

    numLowPulses = 0
    numHighPulses = 0
    for _ in range(1000):
        pulses = deque([(module, "low","broadcaster") for module in adjacent["broadcaster"]])
        numLowPulses += 1 # initial button press
        while len(pulses) > 0:
            l = len(pulses)
            for _ in range(l):
                module, signal, sender = pulses.popleft()
                # print(sender, "-"+signal+"->", module)

                if signal == "low": numLowPulses += 1
                else: numHighPulses += 1
                
                # toggle module
                if moduleType[module] == "%":
                    if signal == "low":
                        newSignal = ""
                        if moduleState[module] == False:
                            moduleState[module] = True
                            newSignal = "high"
                        else:
                            moduleState[module] = False
                            newSignal = "low"
                        
                        for neighbor in adjacent[module]:
                            pulses.append((neighbor, newSignal, module))
                
                # conjunction module
                elif moduleType[module] == "&":
                    if signal == "low":
                        if sender in moduleState[module][1]:
                            moduleState[module][1].remove(sender)
                            moduleState[module][0].add(sender)
                    elif signal == "high":
                        if sender in moduleState[module][0]:
                            moduleState[module][0].remove(sender)
                            moduleState[module][1].add(sender)
                    newSignal = "high"
                    if len(moduleState[module][0]) == 0:
                        newSignal = "low"
                    
                    for neighbor in adjacent[module]:
                        pulses.append((neighbor, newSignal, module))

    return numLowPulses * numHighPulses


print(solution())