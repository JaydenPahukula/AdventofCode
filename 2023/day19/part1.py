d = {"x":0,"m":1,"a":2,"s":3}
def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    workflows = {}
    for i in range(len(data)):
        if data[i] == "":
            data = data[i+1:]
            break
        title, line = data[i].split("{")
        workflows[title] = line.strip("}").split(",")
    
    parts = []
    for line in data:
        parts.append(tuple([int(x[2:]) for x in line[1:-1].split(",")]))
    
    total = 0
    for part in parts:
        wf = "in"
        while wf not in ("A","R"):
            for rule in workflows[wf][:-1]:
                rule, destination = rule.split(":")
                if (rule[1] == ">" and part[d[rule[0]]] > int(rule[2:])) or (rule[1] == "<" and part[d[rule[0]]] < int(rule[2:])):
                        wf = destination
                        break
            else:
                wf = workflows[wf][-1]
        if wf == "A":
            total += sum(part)
    
    return total


print(solution())