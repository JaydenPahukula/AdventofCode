
def solution():

    with open("day05/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines() if x != ""]
    
    stacks = ["RPCDBG", "HVG", "NSQDJPM", "PSLGDCNM", "JBNCPFLS", "QBDZVGTS", "BZMHFTQ", "CMDBF", "FCQG"]

    for line in data:
        instruction = line.split(' ')
        
        stacks[int(instruction[5])-1] += stacks[int(instruction[3])-1][-int(instruction[1]):]
        stacks[int(instruction[3])-1] = stacks[int(instruction[3])-1][:-int(instruction[1])]

    final = ""
    for stack in stacks:
        final += stack[-1]

    return final


print(solution())