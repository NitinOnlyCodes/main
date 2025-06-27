# Problem statement
# You are given two binary grids ‘MAT1’ and ‘MAT2’ of size N x N each. Both grids either have 0 or 1 written in each cell.

# You can perform four types of operations to MAT1-

# • Right Shift
# • Left Shift
# • Up Shift
# • Down Shift
# For eg:

# Let the grid MAT1 be-

#  After one right shift, it will look like-

# After one left shift, it will look like-

# After one up shift, it will look like-

# After one down shift, it will look like-

# You can perform any of the above operations in any order, any number of times(possibly zero) to MAT1.

# Overlap of two grids is defined as the number of cells which have 1 written in it, in both the grids. Your task is to find the maximum possible overlap between ‘MAT1’ and ‘MAT2’ after applying some operations to ‘MAT1’.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 5
# 1 <= N <= 30
# 0 <= MAT1[i][j] <= 1
# 0 <= MAT2[i][j] <= 1

# Time Limit: 1 sec.
# Sample Input 1 :
# 2
# 3 
# 1 1 0
# 0 0 0
# 0 0 0
# 0 1 1
# 0 0 0
# 0 0 0
# 2
# 1 1
# 1 1
# 1 1
# 1 1
# Sample Output 1:
# 2
# 4
# Explanation for Sample 1:
# The optimal answer for the first test case:

# After applying one right shift to MAT1, we get it as-
#   0 1 1
#   0 0 0
#   0 0 0
# The overlap of MAT1 with MAT2 will be 2.


# The optimal answer for the second test case:

# We do not apply any shift to MAT1.
# The overlap of MAT1 with MAT2 will be 4.
# Sample Input 2 :
# 1
# 3  
# 1 1 0
# 0 1 0
# 0 1 0
# 0 0 0
# 0 1 1
# 0 0 1
# Sample Output 2:
# 3

from os import *
from sys import *
from collections import *
from math import *

def gridOverlap(mat1, mat2, n):

	# Write your code here.
	def count_overlap(dx, dy):
		count = 0
		for i in range(n):
			for j in range(n):
				ni, nj = i + dx, j + dy
				if 0 <= ni < n and 0 <= nj < n:
					if mat1[i][j]== 1 and mat2[ni][nj]==1:
						count += 1
		return count
	max_overlap = 0
	for dx in range(-(n-1), n):
		for dy in range(-(n-1), n):
			max_overlap = max(max_overlap, count_overlap(dx, dy))

	return max_overlap