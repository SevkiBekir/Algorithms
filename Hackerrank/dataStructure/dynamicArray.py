def dynamicArray(n, queries):
    s = []
    for i in range(n):
        s.append([])
    
    lastAnswer = 0
    result = []
    for i in range(len(queries)):
        seqIndex = (queries[i][1] ^ lastAnswer) % n
        if queries[i][0] == 1:
           s[seqIndex].append(queries[i][2])
        else:
            lastAnswer = s[seqIndex][queries[i][2] % len(s[seqIndex])]
            result.append(lastAnswer)
    return result

if __name__ == "__main__":
    n = 2
    queryCounter = 5
    sample = "1 0 5 1 1 7 1 0 3 2 1 0 2 1 1"
    arr = list(map(int,sample.rstrip().split()))
    queries = []
    for i in range(0,5):
        q = []
        for j in range(0,3):
            q.append(arr[i*3+j])
        queries.append(q)
    
    # print(queries)
    result = dynamicArray(2,queries)
    print(result)
