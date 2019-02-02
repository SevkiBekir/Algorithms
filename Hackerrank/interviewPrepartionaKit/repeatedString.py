
def repeatedString(s, n):
    
    if len(s) == 1 and s[0] == 'a':
        return n
    
    temp = s
    aCounter = 0
    # find a counter in s
    for char in s:
        if char == 'a':
            aCounter += 1

    aCounter *= int(n/len(temp))
   
    s = temp[:n%len(temp)]
    # find a counter in s for remaining part
    for char in s:
        if char == 'a':
            aCounter += 1

    # return a's counter
    return aCounter




if __name__ == "__main__":
    print("start!")
    
    # s = "aba"
    # n = 10
    # result = repeatedString(s,n)
    # print(result)

    s = "kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"
    n = 202
    result = repeatedString(s,n)
    print(result)
    