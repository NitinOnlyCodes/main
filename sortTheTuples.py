# Problem statement
# You are given an array of tuples ‘ARR’ of length ‘N’. All the tuples are of length ‘L’. Sort the tuples in non-decreasing order by the last element of tuples. If the last element of two tuples are equal then the tuple with the smallest index should be placed first.

# Note: The length of all the tuples will be the same.

# Example:
# Input: ‘N’ = 3, ‘L’ = 2,  ‘ARR’ = [(1, 1), (5, 3), (8, 2)]. 

# Output: [(1, 1), (8, 2), (5, 3)].

# The last values of each type are (1, 3, 2). Sorting them in non-decreasing order we get (1, 2, 3). Hence the final result is [(1, 1), (8, 2), (5, 3)].
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 10
# 1 <= N <= 10^5
# Sum of total number of integers <= 10^5
# 1 <= ARR[i].length <= 1000

# Time Limit: 1 sec
# Sample Input 1 :
# 2
# 4 2
# 1 2
# 1 1
# 3 5
# 2 3
# 4 3
# 1 2 3
# 3 2 1
# 4 5 6
# 3 1 2
# Sample Output 1 :
# 1 1 
# 1 2 
# 2 3 
# 3 5 
# 3 2 1 
# 3 1 2 
# 1 2 3 
# 4 5 6 
# Explanation Of Sample Input 1 :
# For the first case:
# The last elements of the tuples are [2, 1, 5, 3]. Sorting them in non-decreasing order we get [1, 2, 3, 5]. So, the final output is [ (1, 1), (1, 2), (2, 3), (3, 5) ].

# For the second case:
# The last elements of the tuples are [3, 1, 6, 2]. Sorting them in non-decreasing order we get [1, 2, 3, 6]. So, the final output is [ (3, 2, 1), (3, 1, 2), (1, 2, 3), (4, 5, 6) ].
# Sample Input 2 :
# 2
# 1 4
# 1 4 5 7
# 3 4
# 7 81 2 10
# 1 2 4 1
# 90 28 2 19
# Sample Output 2 :
# 1 4 5 7
# 1 2 4 1
# 7 81 2 10
# 90 28 2 19

# from os import *
from sys import *
from collections import *
from math import *

from typing import *

def sortTuples(arr : List[List[int]]):
    # Write your code here.
    for i in range(len(arr)):
        arr[i].append(i)

    arr.sort(key = lambda x: (x[-2], x[-1]))

    for i in range(len(arr)):
        arr[i].pop()

    return arr