# Problem statement
# You are given three integers ‘X’, ‘Y’ and ‘N’. Find the value of division X / Y up to ‘N’ decimal places.

# You should return a string that represents the value X / Y up to ‘N’ decimal places. This string must have ‘N’ digits after decimals. You don’t need to round off the result to ‘N’ decimal places, just find the first ‘N’ places after decimals.

# Note:

# 1. It is guaranteed that division X / Y is always finite.
# Example:

# Consider X = 5, Y = 4 and N = 5, then you should return “1.25000”. 
# Note, here we add 3 trailing zeros so that it has exactly 5 digits after decimals.    
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 50
# -10^8  <= X <= 10^8
# -10^8  <= Y <= 10^8
# Y != 0
# 1 <= N <= 10^4

# Time limit: 1 sec
# Sample Input 1:
# 2
# 5 4 1
# 5 4 5   
# Sample Output 1:
# 1.2
# 1.25000
# Explanation of Sample Input 1:
# Test case 1:
# Division 5/4 = 1.25, but we need to print only ‘1’ digit after decimals, thus we should print 1.2.

# Test case 2:
# See the problem statement for an explanation.
# Sample Input 2:
# 3
# -1 -2 1
# 1 -5 6
# -1 1000 2
# Sample Output 2:
# 0.5
# -0.200000
# -0.00

from os import *
from sys import *
from collections import *
from math import *

def findDivision(x, y, n):
    # Write your code here.
    if y ==0:
        return "0.0"

    sign = "-" if (x < 0)^(y < 0) else ''
    x_Abs = abs(x)
    y_Abs = abs(y)

    int_part = x_Abs // y_Abs
    remainder = x_Abs % y_Abs

    decimal_digit = []
    for _ in range(n):
        remainder *= 10
        digit = remainder // y_Abs
        decimal_digit.append(str(digit))
        remainder = remainder % y_Abs
    result = sign + str(int_part) + '.' + ''.join(decimal_digit[:n])
    return result