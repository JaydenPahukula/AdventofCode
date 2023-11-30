
def solution():

    #read data
    with open("day21/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    #initialize monkeys
    monkeys = {}
    for line in data:
        name = line[:4]
        l = line.split(' ')
        if len(l) > 2:
            monkeys[name] = l[1:]
        else:
            monkeys[name] = int(l[1])
    
    #recursive solution
    def getNum(name):
        x = monkeys[name]
        if type(x) == int:
            return x
        else:
            operation = x[1]
            if operation == '+':
                return getNum(x[0]) + getNum(x[2])
            elif operation == '-':
                return getNum(x[0]) - getNum(x[2])
            elif operation == '*':
                return getNum(x[0]) * getNum(x[2])
            else:
                return int(getNum(x[0]) / getNum(x[2]))

    return getNum("root")


print(solution())