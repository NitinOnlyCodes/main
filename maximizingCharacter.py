# Problem statement
# You are given a string 'S' of 'N' lowercase English characters numbered from '0' to 'N - 1'.



# Also, you have a character 'C' initially equal to 'a'. You will perform 'N' operation to maximize the character 'C'.



# In the 'i-th' operation, you can update 'C' with 'S[i - 1]' if 'S[i - 1]' is equal to 'C + 1' or 'C + 2' or do nothing. Note that it is not necessary to update 'C' if you can.



# Return the maximum value of 'C' after performing all the operations.



# Example:
# N = 4
# S = 'dcba'
# Initially, 'C' is equal to 'a'.
# In the first operation, you will do nothing.
# In the second operation, you will update 'C' to 'c'.
# In the next two operations, you will do nothing. So the final value of 'C' is 'c'.
# It can be proved that we can not have the value of 'C' greater than 'c'.
# So the answer for this case is 'c'. 
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 3 <= 'N' <= 10^5
# 'a' <= 'S[i]' <= 'z'

# Time limit: 1 sec
# Sample input 1:
# 2
# 3
# dea
# 2
# bd
# Sample output 1:
# a
# d
# Explanation of sample input 1:
# For test case 1:
# It can be proved that we can not get the value of 'C' greater than 'a' after performing all the operations.
# So, the answer for this case is 'a'.

# For test case 2: 
# We can update 'C' in both operations. So the final value of 'C' will be 'd'.
# We can see that we can not get the value of 'C' greater than 'd'.
# So the answer for this case is 'd'.
# Sample input 2:
# 2
# 5
# edcba
# 5
# deefb
# Sample output 2:
# c
# b

def maximizeCharacter(n: int, s: str) -> str:
	# Write your code here.
    c = 'a'
    for i in range(n):
        if ord(s[i]) == ord(c) + 1 or ord(s[i]) == ord(c) + 2:
            c = s[i]
    return c
