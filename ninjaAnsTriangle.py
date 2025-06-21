# Problem statement
# Ninja has been given ‘N’ stars. Ninja has to make a triangle using these stars. The ‘i’th’ level of a triangle contains a ‘i’ number of stars.

# Can you help Ninja to make a triangle as large as possible using these stars?

# For example:
# Let the number of stars is 6.

# Then we can make a triangle of maximum height 3.
# Note:
# If the number of stars is 7 in the above example, then also the maximum height of the triangle is 3. This is because to make a triangle of height 4 we need at least 10 stars. So in this case (N = 7) to we will return 3.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= ‘T’ <= 100
# 1 <= ‘N’ <= 10 ^ 8

# Where ‘T’ denotes the total number of test cases and ‘N’ represents the number of stars.

# Time Limit: 1 second
# Sample Input 1:
# 2
# 2
# 5
# Sample Output 1:
# 1
# 2   
# Explanation for Sample Output 1:
# For sample test case 1: 

# In this example, we can make a triangle of height 1 only. For making a triangle of height 2, we need at least 3 stars but we have only 2 stars.

# For sample test case 2: 

# In this example, we can make a triangle of height 2 only. For making a triangle of height 3, we need at least 6 stars but we have only 5 stars.
# Sample Input 2:
# 2
# 6
# 10
# Sample Output 2:
# 3
# 4
# Explanation for Sample Output 2:
# For sample test case 1: 

# In this example, we can make a triangle of height 3.

# For sample test case 2:

# In this example, we can make a triangle of height 4.

from os import *
from sys import *
from collections import *
from math import *

def ninjaAndTriangle(n):
    # Write your code here.
    low = 1
    high = n
    ans= 0
    while low <= high:
        mid = (low + high) // 2
        required = mid * (mid + 1) // 2

        if required <= n:
            ans = mid
            low = mid+1
        else:
            high = mid - 1

    return ans
