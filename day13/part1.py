
def parse(s:str):

    s1 = s[1:-1]
    if len(s1) == 0:
        return []

    final = []
    item = ""
    i = 0
    while i < len(s1):
        if s1[i] == ',':
            final.append(int(item))
            item = ""
        elif s1[i] == '[':
            item += '['
            i += 1
            depth = 1
            while depth > 0:
                if s1[i] == '[':
                    depth += 1
                if s1[i] == ']':
                    depth -= 1
                item += s1[i]
                i += 1
            final.append(parse(item))
            item = ""
        else:
            item += s1[i]

        i += 1
    if item != "":
        final.append(int(item))

    return final

def inOrder(pair):

    left = pair[0]
    right = pair[1]

    i = 0
    while 1:
        if i >= len(left) and i >= len(right):
            return
        if i >= len(left):
            return True
        if i >= len(right):
            return False

        if type(left[i]) == list or type(right[i]) == list:
            if type(left[i]) == list and type(right[i]) != list:
                right[i] = [right[i]]
            elif type(right[i]) == list and type(left[i]) != list:
                left[i] = [left[i]]

            outcome = inOrder((left[i],right[i]))
            if outcome != None:
                return outcome

        else:
            if left[i] > right[i]:
                return False
            if left[i] < right[i]:
                return True
        
        i += 1

    return

def solution():

    with open("day13/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    #parse data
    packets = []
    for ii in range(int((len(data)+1)/3)):
        i = ii*3
        packets.append((parse(data[i]), parse(data[i+1])))
    
    i = 1
    score = 0
    for pair in packets:
        if inOrder(pair):
            score += i
        i += 1

    return score


print(solution())
