# Problem statement
# Given an array ‘A’. Your task is to choose any two different elements of the array say ‘X’ and ‘Y’, such that ‘Z’ is minimum possible. Where ‘Z’ = ‘X’ × ’Y’.



# Return the minimum possible value of ‘Z’.



# Example:
# ‘N’ = [5, 3, 9, 6, 3]

# ‘X’ can be chosen as 3(index 1) and ‘Y’ can be chosen as 3(index 4). 'Z' = 3*3 = 9.
# No other combination can have a smaller value of ‘Z’.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= ‘T’ <= 10
# 2 <= ‘N’ <= 10^5
# -10^4 <= ‘A[i]’ <= 10^4

# Time Limit: 1 sec
# Sample Input 1:
# 2
# 6
# -6 10 -1 2 10 -1 
# 7
# -7 5 -1 -4 -10 -8 10 
# Sample Output 1:
# -60
# -100
# Explanation of sample input 1:
# For 1st Testcase :
# ‘X’ can be chosen as -6(index 0)  and ‘Y’ can be chosen as 10(index 1). 'Z' = -6*10 = -60.
# No other combination can have a smaller value of ‘Z’.

# For 2nd Testcase :
# ‘X’ can be chosen as -10(index 4) and ‘Y’ can be chosen as 10(index 6). 'Z' = -10*10 = -100.
# No other combination can have a smaller value of ‘Z’.
# Sample Input 2:
# 3
# 6
# -5 -10 5 7 -8 -8 
# 6
# -10 6 1 -6 7 5 
# 8
# 0 0 3 -8 -10 -7 4 -5 
# Sample Output 2:
# -70
# -70
# -40

from typing import *

def minimize_z(a: List[int]):
    # Write your code here.

    a.sort()
    min_prod = float('inf')
    n=len(a)
    for i in range(n):
        for j in range(i+1, n):
            prod = a[i] * a[j]
            if prod < min_prod:
                min_prod=prod

            if a[i]==0:
                break
    return min_prod
