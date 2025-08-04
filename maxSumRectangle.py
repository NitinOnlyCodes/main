# Problem statement
# You are given a matrix ‘ARR’ with ‘N’ rows and ‘M’ columns. Your task is to find the maximum sum rectangle in the matrix.

# Maximum sum rectangle is a rectangle with the maximum value for the sum of integers present within its boundary, considering all the rectangles that can be formed from the elements of that matrix.

# For Example
# Consider following matrix:

# The rectangle (1,1) to (3,3) is the rectangle with the maximum sum, i.e. 29.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints
#  1 <= T <= 10
#  1 <= M, N <= 75
#  -10^5 <= ARR[i][j] <= 10^5

# Time Limit: 1 sec
# Sample Input 1
# 2
# 1 2
# -1 1
# 2 2
# -1 1
# 2 2
# Sample Output 1
# 1
# 4
# Explanation of Input 1
# The maximum sum rectangle corresponding to the first test case is-

# The maximum sum rectangle corresponding to the second test case is-

# Sample Input 2
# 1
# 4 5
# 1 2 -1 -4 -20
# -8 -3  4 2 1
# 3  8 10 1 3
# -4 -1 1 7 -6
# Sample Output 2
# 29

from os import *
from sys import *
from collections import *
from math import *

def kadane(arr):
    max_sum = float('-inf')
    curr_sum = 0
    for num in arr:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum=0
    return max_sum

def maxSumRectangle(arr, n, m):

    # write your code here
    max_sum = float('-inf')

    for left in range(m):
        temp = [0]*n
        for right in range(left, m):
            for i in range(n):
                temp[i] += arr[i][right]

            current_max = kadane(temp)
            max_sum = max(max_sum, current_max)
    return max_sum
