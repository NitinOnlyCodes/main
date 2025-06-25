# Problem statement
# Today is the teacher's birthday. She has purchased 'N' chocolates to distribute among 'K' students.



# The teacher distributes the chocolates one at a time. She selects the student who has received the least number of chocolates so far. If there are multiple students with the least number of chocolates, she randomly chooses one of them to give the next chocolate.



# What is the maximum quantity of chocolates a single student could potentially receive?



# Example:
# 'N'= 5
# 'K'= 2
# Let the students be A and B.
# First chocolate is given to A. (randomly chosen between A and B)
# Second chocolate is given to B.
# Third chocolate is given to A. (randomly chosen between A and B)
# Fourth chocolate is given to B.
# Fifth chocolate is given to B. (randomly chosen between A and B)

# Hence maximum quantity of chocolates a single student could potentially receive is 3.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= ‘T’ <= 10
# 1 <= ‘N’ <= 10^5
# 1 <= ‘K’ <= 10^5
# 1 <= ‘A[i]’ <= 10^9

# Time Limit: 1 sec
# Sample Input 1:
# 2
# 21 7
# 26 7
# Sample Output 1:
# 3
# 4
# Explanation of sample input 1:
# For test case 1:
# Since the number of chocolates is divisible by the number of students, the maximum number of chocolates any student can receive is 3.

# For test case 2:
# Given the same number of students as the previous scenario but with an additional 5 chocolates, the teacher continues to randomly select the student with the fewest chocolates. As a result, 5 out of 7 students will receive an extra chocolate, leading to a maximum of 4 chocolates received by any one student.
# Sample Input 2:
# 3
# 72 33
# 47 3
# 97 26
# Sample Output 2:
# 3
# 16
# 4

def teacher_birthday(n: int, k: int):
    # Write your code here.
    quotient = n // k
    remainder = n % k
    max_chocolates = quotient

    if remainder != 0:
        max_chocolates += 1

    return max_chocolates