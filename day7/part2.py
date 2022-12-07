#note: I added "cd .." to the end of the input to get back to root

def solution():

    with open("day7/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    dirs = {}
    currPath = [""]
    i = 0
    while 1:
        #cd
        if data[i][2:4] == "cd":
            #cd ..
            if data[i][5:7] == "..":
                #calculate size of folder as we leave it
                sum = 0
                for item in dirs[currPath[-1]]:
                    if type(item) == int:
                        sum += item
                    else:
                        sum += dirs[item]
                dirs[currPath[-1]] = sum
                currPath.pop(-1)
            #cd dir
            else:
                currPath.append(currPath[-1]+data[i][5:])
                if currPath[-1] not in dirs.keys():
                    dirs[currPath[-1]] = []
                #print("  "*len(currPath), currPath[-1])
        #ls
        elif data[i][2:4] == "ls":
            while (data[i+1][0] != "$"):
                if data[i+1][:3] == "dir":
                    dirs[currPath[-1]].append(currPath[-1]+data[i+1][4:])
                else:
                    dirs[currPath[-1]].append(int(data[i+1].split(" ")[0]))
                i += 1
                if i+1 >= len(data): break
        else:
            print("invalid input")
            return -1
        i += 1
        if i >= len(data): break
    
    need = dirs["/"] - (70000000-30000000)
    min = dirs["/"]
    for size in dirs.values():
        if size < min and size >= need:
            min = size
    return min

print(solution())