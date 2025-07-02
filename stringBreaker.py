# Problem statement
# You are given a string ‘S’ and a set of words named ‘Dictionary’. You can perform the operation of breaking the given string 'S', in any possible way and divide the given string into any number of subparts. Your task is to break the given string 'S', such that all the subparts are present in the Dictionary. You just need to tell the minimum number of times you need to break the string 'S' in order to accomplish the above task.

# Note:
# 1. If string 'S' is already present in the dictionary, then you don’t need to break the string and you can print 0 in such cases.
# 2. If it is impossible to complete the given task, then print -1.
# 3. All the characters of string 'S' and words inside the Dictionary only contain Uppercased English Alphabets.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 50
# 1 <= N <= 10^4
# 1 <= |S| <= 50
# 1 <= |word[i]| <= 50
# ‘A’ <= S[i] <= ‘Z’

# Where |S| denotes the length of the given string, |word[i]| denotes the length of the ith word in the Dictionary.
# It is guaranteed that all the words in the dictionary consist of only uppercase English alphabets from ‘A’ to ‘Z’.

# Time Limit: 1 sec.
# Sample Input 1:
# 1
# CODESTUDIO
# 5
# COD
# CODE
# ESTU
# DIO
# STUDIO
# Sample Output 1:
# 1
# Explanation of sample input 1:
# We can break “CODESTUDIO” once and get subparts as “CODE” and “STUDIO”.
# Sample Input 2:
# 1
# BREAKME
# 3
# BROKE
# ME
# BREAKM
# Sample Output 2:
# -1
# Explanation of sample input 2:
# Since there is no way by which we can break the given string and their subparts will be present in the Dictionary.

from os import *
from sys import *
from collections import *
from math import *

def stringBreaker(s, n, dictionary):
    # Write your code here.
    word_set = set(dictionary)
    length = len(s)
    dp = [float('inf')] * (length + 1)
    dp[0] = 0

    for i in range(1, length+1):
        for j in range(i):
            if s[j:i] in word_set:
                dp[i] = min(dp[i], dp[j] +1)

    if dp[length] == float('inf'):
        return -1
    return dp[length]-1
