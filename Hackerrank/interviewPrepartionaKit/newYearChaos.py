# def minimumBribes(q):
#     step = 0
#     check = 0
#     result = 0
#     for i in range(0,len(q)):
#         check = q[i] -(1 + i)
#         if check > 2:
#             print("Too chaotic")
#             return
#         else:
#             if check >0:
#                 step += check
#     print(step)  
#     return
def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes+=1
    print(bribes)

if __name__ == "__main__":
    arr = "5 1 2 3 7 8 6 4"
    arr = list(map(int,arr.rstrip().split()))
    minimumBribes(arr)
    arr = "1 2 5 3 7 8 6 4"
    arr = list(map(int,arr.rstrip().split()))
    minimumBribes(arr)
    arr = [P-1 for P in arr]
    print(arr)