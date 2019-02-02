def countingValleys(n, s):
    altitude = 0
    valleyCounter = 0
    lockValley = False
    for step in s:
        if step == 'U':
            altitude +=1
        else:
            altitude -=1

        if altitude < 0 and lockValley == False:
            valleyCounter +=1
            lockValley = True
        elif altitude>=0:
            lockValley = False
    return valleyCounter

if __name__ == '__main__':
    n = 8
    s = "UDDDUDUUDDUU"
    result = countingValleys(n,s)
    print(result)