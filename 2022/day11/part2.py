
def solution():

    with open("day11/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    held = []
    monkeyInfo = []
    numMonkeys = int((len(data)+1)/7)
    a = 1
    for ii in range(numMonkeys):
        i = ii*7
        holding = [int(x.replace(',', '')) for x in data[i+1].split(' ')[4:]]
        operation = data[i+2].split(' ')[6]
        operand = data[i+2].split(' ')[7]
        test = int(data[i+3].split(' ')[-1])
        iftrue = int(data[i+4].split(' ')[-1])
        iffalse = int(data[i+5].split(' ')[-1])
        held.append(holding)
        monkeyInfo.append([operation, operand, test, iftrue, iffalse])
        a *= test

    monkeyScore = [0] * numMonkeys
    for round in range(10000):

        for i in range(numMonkeys):

            #extract monkey info
            operation = monkeyInfo[i][0]
            operandTEMP = monkeyInfo[i][1]
            test = monkeyInfo[i][2]
            iftrue = monkeyInfo[i][3]
            iffalse = monkeyInfo[i][4]

            for item in range(len(held[i])):

                monkeyScore[i] += 1

                #set the operand
                if operandTEMP == 'old':    operand = int(held[i][0])
                else:                       operand = int(operandTEMP)

                #change the worry level
                if operation == '+':    held[i][0] += operand
                else:                   held[i][0] *= operand

                held[i][0] = held[i][0] % a

                #pass to next monkey
                if (held[i][0] % test == 0):
                    held[iftrue].append(held[i][0])
                else:
                    held[iffalse].append(held[i][0])
                
                held[i].pop(0)

    monkeyScore.sort()
    return monkeyScore[-1] * monkeyScore[-2]

print(solution())