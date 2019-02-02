def jumpingOnClouds(c):
    length = len(c) - 2
    step = 0
    i = 0
    while i <= length :
        if i != length  and c[i+2] == 0:
            # you can move to cumulus cloud by step 2
            i += 2
            step +=1
        elif c[i+1] == 0:
            i+=1
            step +=1
    
    return step



if __name__ == '__main__':
    n  = 7
    s = "0 0 1 0 0 1 0"
    s = list(map(int, s.rstrip().split()))
    result = jumpingOnClouds(s)
    print(result)

    s = "0 0 0 1 0 0"
    s = list(map(int, s.rstrip().split()))
    result = jumpingOnClouds(s)
    print(result)