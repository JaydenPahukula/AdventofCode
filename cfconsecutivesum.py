#cf consecutive sum

def solution():

    numCases = int(input())
    data = []
    for i in range(numCases*2):
        data.append(input())
    
    for case in range(0, len(data), 2):
        n = int(data[case].split(' ')[0])
        k = int(data[case].split(' ')[1])
        a = [int(x) for x in data[case+1].split(' ')]
        if n == k:
            print(sum(a))
            continue

        seperated = [[] for x in range(k)]
        for i in range(n):
            seperated[i % k].append(a[i])
        
        for ka in seperated:
            ka.sort()
        
        print(sum([b[-1] for b in seperated]))


    return

solution()