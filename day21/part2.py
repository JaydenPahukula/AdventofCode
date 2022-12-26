
def solution(humn:int):

    #read data
    with open("day21/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    #initialize monkeys
    monkeys = {}
    for line in data:
        name = line[:4]
        #override the humn monkey
        if name == 'humn':
            monkeys[name] = humn
            continue
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
                return getNum(x[0]) / getNum(x[2])
    
    #return the difference of the root monkey's comparison
    return getNum(monkeys["root"][0]) - getNum(monkeys["root"][2])

#find a list of possible answers whos outputs are integers (to avoid floating point arithmetic)
l = [n for n in range(1000) if solution(n) % 1 == 0][:2]
#find the difference between two of them, and use that to find the correct input
print(int((l[1]-l[0])*solution(0)/(solution(l[0])-solution(l[1]))))
