# # Problem statement
# # Given two integers ‘Left’ and ‘Right’. Your task is to find the total count of ‘megaprime’ numbers from the range ‘Left’ to ‘Right’. A ‘megaprime’ number is a prime number and its individual digits are also prime.

# # For example, ‘53’ is a ‘megaprime’ number because ‘53’ is a prime number and its individual digits,‘3’ and ‘5’, are also prime. ‘13’ is not a ‘megaprime’ number because out of its individual digits (1, 3), ‘1’ is not prime.

# # Note :

# # 1.’Left’ and ‘Right’ both are inclusive in the range ‘Left’ to ‘Right’.
# # Example :

# # ‘Left’ = ‘23’  and ‘Right’ = ‘37’

# All prime numbers from ‘23’ to ‘37’ are 23, 29, 31, 37

# 23 is ‘megaprime’ number because ‘2’ and ‘3’ both are prime
# 29 is not ‘megaprime’ number because ‘9’ is not a prime
# 31 is not a ‘megaprime’ number because ‘1’ is not a prime number
# 37 is ‘megaprime’ number because ‘3’ and ‘7’ both are prime numbers
# Hence there are two ‘megaprime’ numbers 23, 37 out of 23, 29, 31, 37.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 100
# 1 <= Left <= Right <= 8000

# Time Limit: 1 sec
# Sample Input 1 :
# 2
# 2 15
# 11 24
# Sample Output 1 :
# 4
# 1
# Explanation Of Sample Input 1 :
# Test Case 1:

# ‘Left’ = ‘2’ and ‘Right’ = ‘15’ 

# All prime numbers from ‘2’ to ‘15’ are 2, 3, 5, 7, 11, 13

# 2 is ‘megaprime’ number because its individual digit ‘2’ is prime.
# 3 is ‘megaprime’ number because its individual digit ‘3’ is prime.
# 5 is ‘megaprime’ number because its individual digit ‘5’ is prime.
# 7 is ‘megaprime’ number because its individual digit ‘7’ is prime.
# 11 is not ‘megaprime’ number because its individual digits ‘1’ and ‘1’ both are not prime.
# 13 is not ‘megaprime’ number because its individual digits ‘1’ is not prime.
# Hence because there are four ‘megaprime’ numbers 2, 3, 5, 7 out of 2, 3, 5, 7, 11, 13, we return four.


# Test case 2:


# ‘Left’ = 11 and ‘Right’ = 24 

# All prime numbers from ‘11’ to ‘24’ are 11, 13, 17, 19, 23

# 11 is not a ‘megaprime’ number because its individual digit ‘1’ is not prime.
# 13 is not ‘megaprime’ number because its individual digit ‘1’ is not prime.
# 17 is not ‘megaprime’ number because its individual digit ‘1’ is not prime.
# 19 is not ‘megaprime’ number because its individual digits ‘1’ and ‘9’ both are not prime.
# 23 is ‘megaprime’ number because its individual digits ‘2’ and ‘3’ both are prime.

# Since there is only one ‘megaprime’ number, 23 out of 11 13, 17, 19, 23, we return one.
# Sample Input 2 :
# 2
# 1 11
# 1 100
# Sample Output 2 :
# 4
# 8

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def is_prime(t):
    if t<2:
        return False
    for i in range(2, isqrt(t)+1):
        if t%i==0:
            return False
    return True

def all_prime(t):
    prime_digits = {'2','3','5','7'}
    return all(d in prime_digits for d in str(t))
def countMegaPrimeNumber(left, right):

    # Write your code here
    # Return total number of 'megaprime' number
    count = 0
    for num in range(left, right+1):
        if is_prime(num) and all_prime(num):
            count += 1
    return count


# Taking input using fast I/O
def takeInput():

    numbers = list(map(int, input().strip().split(" ")))

    return numbers


# Main
t = int(input())
while t:
    left, right = takeInput()
    print(countMegaPrimeNumber(left, right))
    t = t-1
