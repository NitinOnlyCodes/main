# Problem statement
# A string ‘S’ is said to be special if each of its characters is one of the first ‘P’ letters of the English alphabet and ‘S’ doesn't contain any palindrome contiguous substring of length 2 or more. You will be given a special string ‘S’ of length ‘N’, find the lexicographically next special string of the same length, or else state that such string does not exist. Print the output string if it exists, otherwise, print "NO" (without quotes).

# A string “s1” is a substring of another string “s2” if “s2” contains the same characters as in “s1”, in the same order and in a continuous fashion also.

# Example: Given a string “cba” and ‘P’ equals 3. So, the next strings which are lexicographically bigger than string ‘S’ are “cbb”, “cbc”, “cca”, “ccb” and “ccc” of size 3. But all of them have a palindrome substring of the size at least 2. So, we will return “NO” as output. If the given string is “cbd” and ‘P’ equals 4 then the next string will be “cda” and it is special. So, we can return an output here.

# Note:

# It is guaranteed that the input string is special.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 10^2
# 1 <= N <= 10^3
# 1 <= P <= 26
# 1 <= |S| <= 10^3

# Time Limit: 1 sec
# Sample Input 1:
# 2
# 4 4
# abcd
# 4 4
# dcbd
# Sample Output 1:
# abda
# NO
# Explanation For Sample Input 1:
# In the first test case, the next string which is lexicographically larger than “abcd” is “abda” and it is special. Thus, we will return it.

# In the second test case, the strings which are lexicographically larger than “dcbd” of length 4 are “dcca”, “dccb”, “dccc”, “dccd”, “dcda”, “dcdb”, “dcdc”, “dcdd”,  “ddaa”, “ddab”, “ddac”, “ddad”, “ddba”, “ddbb”, “ddbc”, “ddbd”, “ddca”, “ddcb”, “ddcc”, “ddcd”, “ddda”, “dddb”, “dddc” and “dddd” which are all not special. Thus, we will return “NO”.
# Sample Input 2:
# 2
# 4 3
# abca
# 2 4
# ad
# Sample Output 2:
# acba
# ba
# Explanation For Sample Input 2:
# In the first test case, the next string which is lexicographically larger than “abca” and also special is “acba” and it is special. Thus, we will return it.

# In the second test case, the next string which is lexicographically larger than “ad” is “ba” and it is special. Thus, we will return it.

from os import *
from sys import *
from collections import *
from math import *

def is_valid(s,i):
    if i>=1 and s[i] == s[i-1]:
        return False
    if i>=2 and s[i] == s[i-2]:
        return False
    return True

def specialString(s, n, p):

    # Write your code here
    # Return a string denoting the answer
    s = list(s)
    for i in range(n-1, -1, -1):
        for c in range(ord(s[i]) + 1, ord('a') + p):
            s[i] = chr(c)
            for j in range(i + 1, n):
                for ch in range(ord('a'), ord('a') + p):
                    s[j] = chr(ch)
                    if is_valid(s, j):
                        break
                else:
                    break
            for j in range(i, n):
                if not is_valid(s, j):
                    break
            else:
                return ''.join(s)

    return "NO"