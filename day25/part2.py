
def DECtoSNAFU(num:int):
    return

def SNAFUtoDEC(s:str):
    return

def solution():

    with open("day25/input.txt", "r") as file:
        data = [x.replace('\n','') for x in file.readlines()]
    
    d = {'=':-2, '-':-1, '0':0, '1':1, '2':2}
    a = {-2:'=', -1:'-', 0:'0', 1:'1', 2:'2'}
    total = [0 for _ in range(max([len(line) for line in data])+5)]
    for line in data:
        for i, c in enumerate(line[::-1]):
            total[i] += d[c]
    print(total)
    for i in range(len(total)):
        print(" ", total[i])
        while total[i] > 2:
            total[i] -= 5
            total[i+1] += 1
        while total[i] < -2:
            total[i] += 5
            total[i+1] -= 1
        print("   ", total[i])
    print(total)
    final = ""
    for num in total:
        final = a[num] + final
    return final.lstrip('0')


print(solution())

#000--10=0-12=21=00-2