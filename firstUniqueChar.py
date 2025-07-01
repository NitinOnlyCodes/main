# Problem statement
# Given a string ‘STR’ consisting of lower case English letters, the task is to find the first non-repeating character in the string and return it. If it doesn’t exist, return ‘#’.

# For example:

# For the input string 'abcab', the first non-repeating character is ‘c’. As depicted the character ‘a’ repeats at index 3 and character ‘b’ repeats at index 4. Hence we return the character ‘c’ present at index 2.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 10 ^ 4

# Where ‘T’ is the number of test cases, and ‘N’ is the length of the string.

# Time Limit: 1 sec
# Sample Input 1:
# 2
# bbabcbcb
# babaabea
# Sample Output 1:
# a
# e
# Explanation of Sample Input 1:
# For the first test case, 
# the first non-repeating character is ‘a’. As depicted the character ‘b’ repeats at index 1, 3, 5, 7, and character ‘c’ repeats at index 6. Hence we return the character ‘a’ present at index 2.

# For the second test case, 
# the character ‘e’ is the first non-repeating character. As depicted the character ‘b’ repeats at index 2, 5, and character ‘a’ repeats at index 3, 4, and 7. Hence we return the character ‘e’ present at index 6.
# Sample Input 2:
# 3
# cbbd
# bebeeed
# abcd
# Sample Output 2:
# c
# d
# a

from os import *
from sys import *
from collections import *
from math import *

def findNonRepeating(str):
    # Write your code here
    # Return a single character
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1 
        else:
            char_count[char] = 1
    for char in str:
        if char_count[char] == 1:
            return char

    return "#"