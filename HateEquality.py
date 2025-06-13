# Problem statement
# There are two strings 'S' and 'T', each having 'N' lowercase English characters. Initially, both strings are equal.



# You don't want the string 'T' equal to 'S'. For this, you can reshuffle the characters of the string 'T'.



# Determine if you can make the string 'T' different from 'S' after reshuffling the characters of the string 'T'.



# Return '1' if you can make the string 'T' different from 'S'. Otherwise, return '0'.



# Example:
# N = 7
# S = 'aab'
# Initially, the string 'T' is equal to 'aab'.
# You can shuffle the characters such that 'T' equals 'aba'. So 'T' is not equal to 'S'.
# So, the answer for this case is '1'.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= 'N' <= 10^5
# 'a' <= S[i] <= 'z'

# Time limit: 1 sec
# Sample input 1:
# 2
# 3
# aaa
# 4
# abcd
# Sample output 1:
# 0
# 1
# Explanation of sample input 1:
# For test case 1:
# It can be proved that you can not shuffle the characters of the string 'T' such that it will be different from 'S'.
# So, the answer for this case is '0'.

# For test case 2:
# Initially, the string 'T' is equal to 'abcd'.
# You can shuffle the characters such that 'T' equals 'dcab'. So 'T' is not equal to 'S'.
# So, the answer for this case is '1'.
# Sample input 2:
# 2
# 6
# abcabc
# 1
# a
# Sample output 2:
# 1
# 0
# Python (3.10)
# 12345
# def canYouMakeDifference(n: int, s: str) -> int:
#     # Write your code here.
#     if s.count(s[0]) == n:
#         return 0
#     return 1
# Last saved at 8:03 PM
# Sample test case
# Custom test case


def canYouMakeDifference(n: int, s: str) -> int:
    # Write your code here.
    if s.count(s[0]) == n:
        return 0
    return 1