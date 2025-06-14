# Problem statement
# You are given an array 'A' of 'N' integers which contains integers in ascending order followed by integers in descending order.

# For example in the array [1, 3, 5, 2, 1], the ascending part is [1, 3, 5], and the descending part is [5, 2, 1].



# You want to find out which part has the larger sum of the values.

# Return '0' if the sum of the values in the ascending part is greater than the descending part, '1' if the sum of the values in the descending part is greater than the ascending part, and '-1' if both the sums are equal.

# Example:
# N = 6
# A = [1, 2, 5, 3, 2]
# The ascending and descending parts of the array are ['1', '2', '5'] and ['5', '3', '2'].
# The sum of the values in descending part i.e., '10' is greater than the ascending part i.e., '8'.
# So the answer for this case is '1'.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= 'N' <= 10^5
# 1 <= A[i] <= 10^5
# There is some fixed value 'j' ('0' <= 'j' <= 'N - 1') such that 'A[i - 1]' < 'A[i]' if 'i' <= 'j' and 'A[i - 1]' > 'A[i]' otherwise.

# Time limit: 1 sec
# Sample input 1:
# 2
# 3
# 1 3 5
# 4
# 1 2 5 3
# Sample output 1:
# 0
# -1
# Explanation of sample input 1:
# For test case 1:
# The ascending and descending parts of the array are ['1', '3', '5'] and ['5'].
# The sum of the values in ascending part i.e., '9' is greater than the descending part i.e., '5'.
# So the answer for this case is '0'.

# For test case 2:
# The ascending and descending parts of the array are ['1', '2', '5'] and ['5', '3'].
# The sum of the values in ascending part i.e., '8' is the same as the descending part i.e., '8'.
# So the answer for this case is '-1'.
# Sample input 2:
# 2
# 6
# 1 2 3 4 2 1
# 3
# 5 2 1
# Sample output 2:
# 0
# 1

from typing import *

def find_the_larger(n: int, v: List[int]):
    # Write your code here.
    left = 0
    right = 0
    for i in range(n):
        if i==0 or v[i] > v[i-1]:
            left += v[i]
        if i == n-1 or v[i]>v[i+1]:
            right += v[i]

    if left == right:
        return -1
    elif left>right:
        return 0

    else:
        return 1

