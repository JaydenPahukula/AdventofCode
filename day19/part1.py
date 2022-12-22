
def solution():

    with open("day19/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    blueprints = []
    for line in data:
        bp = []
        bp.append([int(line.split(' ')[6]), 0, 0])
        bp.append([int(line.split(' ')[12]), 0, 0])
        bp.append([int(line.split(' ')[18]), int(line.split(' ')[21]), 0])
        bp.append([int(line.split(' ')[27]), 0, int(line.split(' ')[30])])
        blueprints.append(bp.copy())

    for bp in blueprints:
        
        q = [([1, 0, 0, 0], "", [0, 0, 0, 0])]

        for min in range(24):
            print("minute", min, "===============")

            l = len(q)
            print(l)
            for i in range(l):
                (robots, path, inventory), *q = q
                #print(robots, inventory, path)

                for material in range(4):
                    inventory[material] += robots[material]

                q.append((robots, path+"-", inventory))
                
                for j, robotBP in enumerate(bp):
                    for material in range(3):
                        if inventory[material] < robotBP[material]:
                            break
                    else:
                        #print("bought", robotBP)
                        newRobots = robots.copy()
                        newRobots[j] += 1
                        newInventory = [inventory[i]-robotBP[i] for i in range(3)]
                        newInventory.append(inventory[3])
                        q.append((newRobots, path+str(j), newInventory))

            input()
            
        print([item[2] for item in q])

        input()


    return blueprints


print(solution())