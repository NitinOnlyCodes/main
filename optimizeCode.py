# Problem statement
# While practicing questions on data structures, Ninja faced a problem and was not able to pass all the test cases of a question as the time complexity of the code Ninja made was very large. Ninja asked you for help. You are given a snippet of code and you have to optimize the code.

# Pseudocode:

# RES = 0
# FOR(i -> A to B) {
#     FOR(j -> C to D) {
#         ADD (i ^ j) to RES;
#     }
# }
# PRINT(RES)
# You are given the integers ‘A’, ‘B’, ‘C’, and ‘D’, and ‘^’ represents the bitwise XOR operator. As the result can be large print the result modulo 1000000007.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 10
# 1 <= A <= B <= 5*10^3
# 1 <= C <= D <= 5*10^3

# Time Limit : 1 sec
# Sample Input 1 :
# 2
# 2 3 7 8
# 1 1 1 1
# Sample Output 1 :
# 30
# 0
# Explanation For Sample Input 1 :
# For the first test case :

# The operations performed will be : 2^7 + 2^8 + 3^7 + 3^8 = 5 + 10 + 4 + 11 = 30

# For the second test :

# The operations performed will be : 1^1 + 1^1 = 0 + 0 = 0
# Sample Input 2 :
# 2
# 3 5 4 5
# 1 2 3 4
# Sample Output 2 :
# 15
# 14

from typing import List

mod = 1000000007
def optimizeCode(a: int, b: int, c: int, d: int) -> int:
    # write your code here
    total = 0
    for bit in range(0,31):
        mask = 1 << bit
        cnt_a_b = ((b+1)// (mask << 1)) * mask
        rem = (b+1) % (mask << 1)
        cnt_a_b += max(0, rem - mask)

        cnt_a_b_prev = ((a)// (mask << 1))* mask
        rem_prev = (a)%(mask << 1)
        cnt_a_b_prev += max(0, rem_prev - mask)
        count1_x = cnt_a_b - cnt_a_b_prev

        cnt_c_d = ((d + 1) // (mask << 1)) * mask
        rem = (d+1) % (mask << 1)
        cnt_c_d += max(0, rem - mask)

        cnt_c_d_prev = ((c) // (mask << 1)) * mask
        rem_prev= (c) % (mask << 1) 
        cnt_c_d_prev += max(0, rem_prev - mask)
        count1_y = cnt_c_d - cnt_c_d_prev

        count0_x = (b - a + 1) - count1_x
        count0_y = (d - c + 1) - count1_y

        total += (count1_x * count0_y + count0_x * count1_y) * mask
        total %= mod
    return total
    
