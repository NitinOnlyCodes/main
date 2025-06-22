# Problem statement
# You are given a string S containing only uppercase English characters. Find whether S is the same as its reflection in the mirror.

# For Example, S = “AMAMA” is the same as its reflection in the mirror.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints
# 1 <= T <=10
# 1 <= Length(S) <= 10 ^ 5

# Where ‘T’ is the number of test cases, ‘S’ is the string given in input.

# Time limit: 1sec.
# Sample Input 1:
# 1
# ITATI
# Sample Output 1:
# YES
# Explanation of sample input 1:
# String “ITATI” is the same as its reflection in the mirror.
# Sample Input 2:
# 2
# MMMM
# MZM
# Sample Output 2:
# YES
# NO

from os import *
from sys import *
from collections import *
from math import *

def isReflectionEqual(s):
    # Write your code here.
    symmetric = {"A","H","I","M","O","T","U","V","W","X","Y"}

    # str1 = "AHIMOTUVWXY"

    # for i in s:
        # symmetric[i] =1

    # n = len(s)

    for i in s:
        if i not in symmetric:
            return False

    rev = s[::-1]

    if rev == s:
        return True

    else:
        return False