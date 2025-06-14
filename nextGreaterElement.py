# Problem statement
# You have been given an array/list ‘ARR’ consisting of ‘N’ positive integers. Your task is to return the Next Greater Element(NGE) for every element.

# The Next Greater Element for an element ‘X’ is the first element on the right side of ‘X’ in the array 'ARR', which is greater than ‘X’. If no such element exists to the right of ‘X’, then return -1.

# For example:
# For the given array 'ARR' = [7, 12, 1, 20]

# The next greater element for 7 is 12.
# The next greater element for 12 is 20. 
# The next greater element for 1 is 20. 
# There is no greater element for 20 on the right side.

# So, the output is [12, 20, 20, -1].
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 100
# 1 <= N <= 5 * 10^3
# 1 <= ARR[i] <= 10^9

# Time Limit: 1 sec
# Sample Input 1:
# 1
# 4
# 13 7 6 12
# Sample Output 1:
# -1 12 12 -1
# Explanation For Sample Output 1:
# For the given array [13, 7, 6, 12].

# There is no greater element for 13 on the right side.
# The next greater element for 7 is 12. 
# The next greater element for 6 is 12. 
# There is no greater element for 12 on the right side.

# So, the output is [-1, 12, 12, -1].
# Sample Input 2:
# 2
# 5
# 1 2 3 4 5
# 3 
# 10 9 10
# Sample Output 2:
# 2 3 4 5 -1
# -1 10 -1

from os import *
from sys import *
from collections import *
from math import *

def nextGreaterElement(arr, n):
	# Write your code here.
	result = [-1]*n
	stack=[]

	for i in range(n-1,-1,-1):
		while stack and stack[-1]<=arr[i]:
			stack.pop()

		if stack:
			result[i] = stack[-1]

		stack.append(arr[i])
	return result