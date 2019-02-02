#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    couples = []
    pairCounter = 0
    for i in ar:
        if i in couples:
            couples.remove(i)
            pairCounter+=1
        else:
            couples.append(i)
    
    return pairCounter



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
