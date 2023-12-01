
d = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}

def solution():

    with open("input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]

    out = 0
    for line in data:
        num = 0
        for i in range(len(line)):
            for key, val in d.items():
                if i + len(key) < len(line)+1 and line[i:i+len(key)] == key:
                    num += 10 * val
                    break
            else: continue
            break
        for i in range(len(line),-1,-1):
            for key, val in d.items():
                if i + len(key) <= len(line) and line[i:i+len(key)] == key:
                    num +=  val
                    break
            else: continue
            break
        out += num
    
    return out


print(solution())