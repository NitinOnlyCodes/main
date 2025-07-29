# Problem statement
# You are given an array/list consisting of 0 and 1 only. Your task is to find the sum of the number of subarrays that contains only 1 and the number of subarrays that contains only 0.

# An array 'C' is a subarray of array 'D' if 'C' can be obtained from 'D' by deletion of several elements from the beginning and several elements from the end. Example :

# Let 'ARR' = [1,0,0] then the possible subarrays of 'ARR' will be: {1}, {0}, {0}, {1,0}, {0,0}, {1,0,0}.
# Example
# If the given array 'ARR' = [1,0,0,0,1,1,0,1]
# Then the number of 1’s subarrays will be 5. [{1},{1},{1},{1,1},{1}]
# And the number of 0’s subarrays will be 7. [{0},{0},{0},{0,0},{0,0},{0,0,0},{0}]
# So our answer will be 5 + 7 = 12.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:-
# 1 <= T <= 100
# 1 <= N <= 5000
# 0 <= ARR[i] <= 1

# Where ARR[i] denotes the elements of the array.

# Time Limit: 1 sec
# Sample Input 1:
# 2
# 7
# 1 0 0 0 1 0 1
# 8
# 1 0 1 0 1 0 1 0 
# Sample Output 1:
# 10
# 8
# Explanation Of Sample Input 1:
# Test case 1: Here ARR = {1,0,0,0,1,0,1}, so number of 1’s subarray is 3 [{1}, {1}, {1}], and number of 0’s subarray is 7 [{0}, {0},{0}, {0,0}, {0,0}, {0,0,0}, {0}].

# Hence the output will be 3 + 7 = 10.

# Test case 2: Here ARR = {1,0,1,0,1,0,1,0} so number of 1’s subarray is 4 [{1}, {1}, {1}, {1}], and the number of 0’s subarray is 4; [{0}, {0}, {0}, {0}].

# Hence the output will be 4 + 4 = 8.
# Sample Input 2:
# 2
# 6
# 1 1 1 1 1 1
# 8
# 1 0 0 0 0 0 0 1
# Sample Output 2:
# 21
# 23
# Explanation Of Sample Input 2:
# Test case 1: Here ARR = {1, 1, 1, 1, 1, 1}, so number of 1’s subarray is 21, and number of 0’s subarray is 0.Hence the output will be 21 + 0 = 21.

# Test case 2: Here ARR = {1, 0, 0, 0, 0, 0, 0, 1} so number of 1’s subarray is 2, and the number of 0’s subarray is 21.Hence the output will be 2 + 21 = 23.

from os import *
from sys import *
from collections import *
from math import *

def numberofSubarrays(arr, n):
    # Write your code here.
    i = 0
    count = 0
    while i < n:
        current = arr[i]
        length = 0

        while i < n and arr[i] == current:
            length += 1
            i += 1

        count += (length * (length + 1))//2

    return count