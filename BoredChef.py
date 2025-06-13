# Problem statement
# You are given a string ‘S’ of size ‘N’ where each character is numbered from ‘0’ to ‘N - 1’. You are allowed to swap any two adjacent characters any number of times.



# You are also given an integer ‘K’. Your task is to check whether it is possible to group any same ‘K’ characters by using the given operation.



# Your task is to tell whether it is possible to group any same ‘K’ characters and return ‘1’ if it is possible, otherwise return ‘0’.

# Example:
# ‘N’ = 5
# ‘K’ = 2
# ‘S’ = “acdab”

# In the first operation, you can swap ‘0th’ and the ‘1st’ character. You’ll get the string ‘S’ as: “cadab”

# In the second operation, you can swap ‘1st’ and the ‘2nd’ character. You’ll get the string ‘S’ as: “cdaab”.

# Here, we are getting a group of two ‘a’s together. Hence, the answer for this test case is ‘1’.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= ‘T’ <= 10
# 1 <= ‘N’ <= 10^5
# 1 <= ‘K’ <= ‘N’
# ‘a’ <= ‘S[i]’ <= ‘z’

# Time Limit: 1 sec
# Sample Input 1:
# 2
# 4 3
# abaa 
# 4 2
# abcd
# Sample Output 1:
# 1
# 0
# Explanation of sample input 1:
# For test case 1:
# In the first operation, swap ‘0th’ and the ‘1st’ element. You’ll get the string ‘S’ as: “baaa”

# Here, the substring from index ‘1’ to ‘3’ contains a group of ‘3’ ‘a’s. Hence, the answer for this test case is ‘1’.

# For test case 2:
# Here, it is impossible to group ‘2’ same characters. So, the answer for this test case is ‘0’.
# Sample Input 2:
# 2
# 5 3
# zzzzz 
# 4 1
# fghe
# Sample Output 2:
# 1
# 1
# Python (3.10)
# 123456781112131415179101618
#         for i in range(0,n):
#             if s[i] == chr(ch):
#                 cnt +=1
#         if cnt >= k:
#             ans = 1
#             break
            
#     return ans
# Last saved at 8:19 PM
# Sample test case
# Custom test case


from typing import *


def bored_chef(n: int, k: int, s: str) -> int:
    # Write your code here.
    
    
    ans=0
    for ch in range(ord('a'), ord('z')+1):
        cnt=0
        for i in range(0,n):
            if s[i] == chr(ch):
                cnt +=1
        if cnt >= k:
            ans = 1
            break
            
    return ans