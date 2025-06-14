# Problem statement
# You've hacked into a game and discovered that your high score is represented by a very long integer 'N' in string format. The hack allows you to rearrange the digits of your current high score.



# Your task is to find and return a string 'A' that represents the maximum possible high score you can achieve by permuting the digits.



# Example:
# ‘N’ = ‘122’

# Return 221
# Any other permutation is smaller than or equal to ‘221’.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= ‘T’ <= 10
# 1 <= |N| <= 10^5 |N| represents the length of the string ‘N’

# Time Limit: 1 sec
# Sample Input 1:
# 2
# 454106
# 6144136
# Sample Output 1:
# 654410
# 6644311
# Explanation of sample input 1:
# For 1st Test Case:
# Any other permutation is smaller than or equal to ‘654410’.

# For 2nd Test Case:
# Any other permutation is smaller than or equal to ‘6644311’.
# Sample Input 2:
# 3
# 117668
# 185977
# 92280947
# Sample Output 2:
# 876611
# 987751
# 99874220

'''
    Time Complexity: O(N)
    Space Complexity: O(1)

    where 'N' is length of the input string.
'''

from typing import *

def hack(n: str) -> str:
    # Bucket Sorting.
    # Calculating the frequency of each digit.
    freq = [0] * 10
    for digit in n:
        freq[int(digit)] += 1

    # Forming the largest number.
    pos = 0
    sorted_digits = []
    for i in range(9, -1, -1):
        for j in range(freq[i]):
            sorted_digits.append(str(i))

    return ''.join(sorted_digits)