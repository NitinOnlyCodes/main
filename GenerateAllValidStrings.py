# Problem statement
# Ninja has been given a string ‘STR’ containing ‘(‘ and ‘)’. ‘STR’ may also contain lower case alphabets. In order to make ‘STR’ valid Ninja can remove either ‘)’ or ‘(’ from ‘STR’.

# Here are some examples of valid ‘STR’ “((a))”, “(g)()”, “(())()”, "" (an empty string is also a valid string).

# Ninja wants to know all the possible valid strings that can be formed from ‘STR’ by minimum possible removals (possibly zero).

# Can you help Ninja to generate all valid strings from ‘STR’ by minimum removals?

# For Example :
# For the given ‘STR’ =  “()(()”, we can form a valid string “()()” by removing ‘(‘ at index 2 or 3.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= ‘T’ <= 100
# ‘STR[i]’ = ‘(‘, ‘)’ or Lower case english alphabet
# 1 <= |STR| <= 2000

# Where |STR| denotes the length of the given string.

# Time Limit: 1 sec
# Sample Input 1 :
# 2
# ()())
# ()(x))()
# Sample Output 1 :
# ()() (())
# ()(x)() ((x))()
# Explanation for Sample Output 1 :
# For the first test case:
# All the valid unique strings that can be formed from “()())” are “()()”, ”()”, ”(())”, ” ” among which “()()”, “(())” are formed from only 1 ‘)’ removal which is the minimum among all.   

# For the second test case:
# All the valid unique strings that can be formed from “()(x))()” are “()(x)()”, ”()()”, ”(())”, ”((x))”, ”(x)”, ”(x)()”, ”((x))()”, ” ” among which ”((x))()” and  “()(x)()” are formed from only 1 ‘)’ removal at index 1 and 5 respectively which takes the minimum removals among all possible valid strings.   
# Sample Input 2 :
# 2   
# ))a((
# (()s())
# Sample Output 2 :
# a
# (()s())
# Explanation for Sample Output 2 :
# For the first test case:
# All the valid unique strings that can be formed from “))a((” are “a” and “” (empty string is also a valid string) in which “a” is formed from 2 ‘)’ removals at index 0 and 1 and 2 ‘(’ removal at index 3 and 4. which is the minimum among all possible valid strings.   

# For the second test case:
# All the valid unique strings that can be formed from “ (()s())” are “()(s)()”, ”((())”, ”(s)”, ”(()s)”, ”(s())”, ”(()s())”, ” ”, ”s”, ”((s)), "()s()” among which "(()s())” is formed from 0 removals which is the minimum possible removals.   


from os import *
from sys import *
from collections import *
from math import *

from collections import deque
def isValid(str):
	count = 0
	for ch in str:
		if ch == '(':
			count += 1
		elif ch == ')':
			count -= 1
		if count < 0:
			return False
	return count == 0

def minRemovaltoMakeStringValid(str):
	# Write your code here.
	if not str:
		return ""
	result=[]
	visited = set()
	queue =deque()
	found = False

	queue.append(str)
	visited.add(str)
	while queue:
		current = queue.popleft()

		if isValid(current):
			result.append(current)
			found = True

		if found:
			continue

		for i in range(len(current)):
			if current[i] not in ('(',')'):
				continue

			temp = current[:i] + current[i+1:]

			if temp not in visited:
				visited.add(temp)
				queue.append(temp)

	return sorted(list(set(result)))
