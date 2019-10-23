def rotLeft(a, d):
    for _ in range(d):
        popElement = a.pop(0)
        a.append(popElement)
    return a

if __name__ == "__main__":
    d = 4
    a = "1 2 3 4 5"
    a = list(map(int,a.rstrip().split()))
    print(rotLeft(a,d))