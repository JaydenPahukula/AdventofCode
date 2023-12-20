from collections import deque

def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    workflows = {}
    for i in range(len(data)):
        if data[i] == "":
            break
        title, line = data[i].split("{")
        workflows[title] = line.strip("}").split(",")
    
    total = 0
    parts = deque([("in",1,4000,1,4000,1,4000,1,4000)])
    while parts:
        wf,lx,hx,lm,hm,la,ha,ls,hs = parts.popleft() # lo-x, hi-x, lo-m, ...

        if lx > hx or lm > hm or la > ha or ls > hs:
            continue
        if wf == "R":
            continue
        if wf == "A":
            total += (hx-lx+1)*(hm-lm+1)*(ha-la+1)*(hs-ls+1)
            continue

        for rule in workflows[wf][:-1]:
            rule, destination = rule.split(":")
            amount = int(rule[2:])
            if rule[0] == "x":
                if rule[1] == ">" and hx > amount:
                    parts.append((destination,max(lx,amount+1),hx,lm,hm,la,ha,ls,hs))
                    hx = amount
                if rule[1] == "<" and lx < amount:
                    parts.append((destination,lx,min(hx,amount-1),lm,hm,la,ha,ls,hs))
                    lx = amount
            elif rule[0] == "m":
                if rule[1] == ">" and hm > amount:
                    parts.append((destination,lx,hx,max(lm,amount+1),hm,la,ha,ls,hs))
                    hm = amount
                if rule[1] == "<" and lm < amount:
                    parts.append((destination,lx,hx,lm,min(hm,amount-1),la,ha,ls,hs))
                    lm = amount
            elif rule[0] == "a":
                if rule[1] == ">" and ha > amount:
                    parts.append((destination,lx,hx,lm,hm,max(la,amount+1),ha,ls,hs))
                    ha = amount
                if rule[1] == "<" and la < amount:
                    parts.append((destination,lx,hx,lm,hm,la,min(ha,amount-1),ls,hs))
                    la = amount
            else:
                if rule[1] == ">" and hs > amount:
                    parts.append((destination,lx,hx,lm,hm,la,ha,max(ls,amount+1),hs))
                    hs = amount
                if rule[1] == "<" and ls < amount:
                    parts.append((destination,lx,hx,lm,hm,la,ha,ls,min(hs,amount-1)))
                    ls = amount
        parts.append((workflows[wf][-1],lx,hx,lm,hm,la,ha,ls,hs))
    
    return total


print(solution())