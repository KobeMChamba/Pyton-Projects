#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    s = list(s)
    s2=s.copy()
    for i in range(int(n/2)+1):
        if s[i]!=s[n-i-1]:
            s[i]=s[n-i-1]=max(s[i], s[n-i-1])
            k-=1
        if k<0:
            return '-1'
    
    i=0
    while k>0 and i<int(n/2)+1:
        if s[i]!='9':
            if s[i]==s2[i] and s[n-i-1]==s2[n-i-1] and i!=n-i-1:
                if k>=2:
                    s[i]=s[n-i-1]='9'
                    k-=2
            else:
                s[i]=s[n-i-1]='9'
                k-=1
        i+=1
        
    return ''.join(s)
              
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
