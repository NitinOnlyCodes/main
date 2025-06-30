# Problem statement
# You have been given a positive integer N. Your task is to find the Nth term of the Look-And-Say sequence.

# The Look-And-Say sequence is a sequence of positive integers. The sequence is as follows:

# 1, 11, 21, 1211, 111221, 312211, 13112221,...

# This sequence is constructed in the following way:

# The first number is 1.

# This is read as “One 1”. 
# Hence, the second number will be 11.

# The second number is read as “Two 1s”. 
# Hence, the third number will be 21.

# The third number is read as “One 2, One 1”. 
# Hence, the fourth number will be 1211.

# The fourth term is read as “One 1, One 2, Two 1s”.
# Hence, the fifth term will be 111221. And so on.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 40

# Time Limit: 1 sec
# Sample Input 1:
# 3
# 1
# 2
# 3
# Sample Output 1:
# 1
# 11
# 21
# Explanation for Sample 1:
# The first term is 1.
# The second term is 11.
# The third term is 21.
# Sample Input 2:
# 1
# 6
# Sample Output 2:
# 312211

from os import *
from sys import *
from collections import *
from math import *

def lookAndSaySequence(n):

	# Write your code here
	if n == 1:
		return "1"

	term = "1"

	for _ in range(1, n):
		next_term = ""
		i = 0

		while i < len(term):
			count = 1

			while i + 1 < len(term) and term[i] == term[i + 1]:
				i += 1
				count += 1
			next_term += str(count) + term[i]

			i += 1
		term = next_term
	return term