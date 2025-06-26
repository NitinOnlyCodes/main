# Problem statement
# You are given a sorted array 'ARR' and a number 'X'. Your task is to count the number of occurrences of 'X' in 'ARR'.

# Note :
# 1. If 'X' is not found in the array, return 0.
# 2. The given array is sorted in non-decreasing order.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 10^2
# 1 <= N <= 10^4
# 0 <= ARR[i], X <= 10^9

# Time Limit : 1 sec
# Sample Input 1 :
# 2
# 7
# 1 1 2 2 2 2 3
# 2
# 5
# 1 2 2 3 3
# 4
# Sample Output 1 :
# 4
# 0
# Explanation For Sample Input 1 :
# For the first test case, the target element 2 occurs four times in the array at indexes from 2 to 5. 

# For the second test case, the target element 4 doesn’t occur in the array.
# Sample Input 2 :
# 2
# 4
# 2 3 4 4
# 4
# 6
# 5 7 7 8 8 10
# 10
# Sample Output 2 :
# 2
# 1

def countOccurrences(arr, x):
    # Write your code here.
    n= len(arr)
    left = 0
    right = n - 1
    first = -1

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == x:
            first = mid
            right = mid - 1

        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1
    if first == -1:
        return 0

    left = 0
    right = n-1
    last = -1

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == x:
            last = mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return last - first + 1
