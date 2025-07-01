# Problem statement
# You have given a 2-dimensional array ‘ARR’ with ‘N’ rows and ‘M’ columns. The queries are given in a 2-dimensional array ‘Queries’ of size ‘K’, in which Queries[i] contains four integers denoting the left top and right bottom indices of the submatrix whose sum we need to find. Your task is to find the sum of the submatrix for each query given in the array ‘Queries’.

# For example:

# Consider ARR = [[1 , 2 , 3] , [3 , 4 , 1] , [2 , 1 , 2]] and Queries = [[0 , 0 , 1 , 2]], the submatrix with the left top index (0 , 0) and right bottom index (1 , 2) is  
#                       [[1 , 2 , 3] , 
#                        [3 , 4 , 1]]. 
# The sum of the submatrix is 14. Hence, the answer is 14 in this case.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
#  1 <= N <= 10 ^ 3     
#  1 <= M <= 10 ^ 3
#  1 <= K <= 10 ^ 3
#  1 <= ARR[i][j] <= 10 ^ 6
#  0 <= Queries[i][0] , Queries[i][2] < N
#  0 <= Queries[i][1] , Queries[i][3] < M 

#  Where 'T' denotes the number of test cases, 'N' and 'M' denotes the number of rows and the number of columns in the array ‘ARR’ respectively, ’K’ denotes the number of rows in the array ‘Queries’, 'ARR[i][j]' denotes the ’j-th’ element of  'i-th' row of the array 'ARR' and 'Queries[i]' contains four integers denoting the left top and right bottom indices of the submatrix.  

# Time Limit: 1sec
# Sample Input 1 :
# 2
# 2 2 1
# 4 2 
# 1 3 
# 0 0 1 0
# 3 3 2
# 2 1 2
# 3 2 6 
# 1 4 5
# 1 1 2 2
# 0 1 0 2
# Sample Output 1 :
# 5
# 17 3   
# Explanation of sample input 1:
# For the first test case, 
# The submatrix with the left top index (0 , 0) and right bottom index (1 , 0) is  
#                           [[4] , 
#                            [1]]. 
# The sum of the submatrix is 5. Hence, the answer is 5 in this case.

# For the second test case,
# The submatrix with the left top index (1 ,1) and right bottom index (2 , 2) is  
#                           [[2 , 6] , 
#                            [4 , 5]]. 
# The sum of the submatrix is 17. Hence, the answer is 17 in this case.

#  The submatrix with the left top index (0 , 1) and right bottom index (0 , 2) is  
#                           [[1 , 2]].  
# The sum of the submatrix is 3. Hence, the answer is 3 in this case.
# Sample Input 2 :
# 2
# 2 2 2
# 5 6 
# 7 5 
# 0 0 0 0
# 0 0 1 1
# 3 3 2
# 3 4 3
# 4 3 4 
# 1 1 1
# 0 0 0 2
# 0 0 2 1
# Sample Output 2 :
# 5 23
# 10 16

from os import *
from sys import *
from collections import *
from math import *

def findSubmatrixSum(arr, queries):
    # Write your code here
    n = len(arr)
    m = len(arr[0])

    prefix = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            prefix[i][j] = arr[i][j]
            if i > 0:
                prefix[i][j] += prefix[i-1][j]
            if j > 0:
                prefix[i][j] += prefix[i][j-1]
            if i > 0 and j > 0:
                prefix[i][j] -= prefix[i-1][j-1]

    result = []
    for x1, y1, x2, y2 in queries:
        total = prefix[x2][y2]
        if x1>0:
            total -= prefix[x1 - 1][y2]
        if y1 > 0:
            total -= prefix[x2][y1-1]
        if x1 > 0 and y1 > 0:
            total += prefix[x1-1][y1-1]
        result.append(total)
    return result
