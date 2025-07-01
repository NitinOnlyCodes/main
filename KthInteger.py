# Problem statement
# You are given an array ‘A’ of ‘N’ distinct integers numbered from ‘0’ to ‘N - 1’. You are also given another two integers ‘K’ and ‘X’. Your task is to find the ‘kth’ smallest number among all those numbers which are not divisible by ‘X’ in the array ‘A’.



# Your task is to tell the ‘kth’ smallest number among all those numbers which are not divisible by ‘X’ and return it. If it doesn't exist, return “-1”.

# Example:
# ‘N’ = 5
# ‘A’ = [10, 1, 9, 2, 18]
# ‘K’ = 2
# ‘X’ = 3

# The numbers which are not divisible by ‘3’ are: [10, 1, 2].

# Here, the ‘2nd’ smallest number is ‘2’.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= 'T' <= 10
# 1 <= 'N' <= 10^5
# 1 <= 'K' <= 'N'
# 1 <= ‘X’ <= 10^9
# 1 <= A[i] <= 10^9

# Time Limit: 1 sec 
# Sample Input 1:
# 2
# 4 1 2
# 2 4 7 9
# 5 3 3
# 3 6 9 12 15
# Sample Output 1:
# 7
# -1
# Explanation of sample input 1:
# For test case 1:
# Here, the numbers which are not divisible by ‘2’ are: [7, 9].

# The ‘1st’ smallest number among all these numbers is ‘7’.

# For test case 2:
# Here, all the numbers are divisible by ‘3’. So, the answer for this test case is ‘-1’.
# Sample Input 2:
# 2
# 5 2 3
# 10 3 27 81 9
# 2 2 10
# 1 5
# Sample Output 2:
# -1
# 5

from typing import *

def kth_integer(n: int, k: int, x: int, a: List[int]):
    not_divisible = []

    for i in range(n):
        if a[i] % x != 0:
            not_divisible.append(a[i])

    not_divisible.sort()

    if len(not_divisible) < k:
        return -1
    else:
        return not_divisible[k-1]