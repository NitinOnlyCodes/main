# Problem statement
# You are given an '0' indexed array 'A' of 'N' integers containing positive and negative integers.



# You want the sum of some subarray of the array 'A' to be maximum. For that, you can rearrange the elements of the array. Note that an empty subarray is considered to be a subarray with sum equal to '0'.



# Return the maximum possible subarray sum after rearranging the elements of the array 'A'.



# Example:
# N = 5
# A = [1, -5, 1, 1, -4]
# We can rearrange the elements as follows: ['1', '1', '1', '-4', '-5']. The maximum subarray sum is '3' for the subarray of the first three elements.
# It can be proved that we can not get the subarray sum greater than '3'.
# So the answer for this case is '3'.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= 'N' <= 10^5
# -10^3 <= 'A[i]' <= 10^3

# Time limit: 1 sec
# Sample input 1:
# 2
# 3
# 1 2 3
# 5
# 2 -2 2 -3 -3
# Sample output 1:
# 6
# 4
# Explanation of sample input 1:
# For test case 1:
# The maximum subarray sum is '1 + 2 + 3' = '6'.
# So the answer for this case is '6'. 

# For test case 2:
# We can rearrange the elements as follows: ['-2', '2', '2', '-3', '-3']. The maximum subarray sum is '4' for the subarray consisting of the second and third elements.
# It can be proved that we can not get the subarray sum greater than '4'.
# So the answer for this case is '4'.    
# Sample input 2:
# 2
# 5
# 1 0 -1 0 1
# 3
# -1 -2 -3
# Sample output 2:
# 2
# 0

def maximumSubarraySum(n: int, v: list[int]) -> int:
   # Write your code here.
   count = 0
   for i in range(len(v)):
      if v[i] > 0:
         count += v[i]
   return count