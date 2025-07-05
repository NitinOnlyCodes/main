# Problem statement
# You are given two LinkedList of length ‘N’. Your task is to insert the elements of the second LinkedList in the first LinkedList at the alternate positions.

# For example: Let 1 -> 3 -> 5 be the first LinkedList and 2 -> 4 -> 6 be the second LinkedList. Then after merging the first LinkedList will look like 1 -> 2 -> 3 -> 4 -> 5 -> 6.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints -
# 1 <= ‘T’ <= 10
# 1 <= ‘N’ <= 10^5
# All the elements in both of the LinkedList lie in the range [-10^9, 10^9] - {1}.
# Note- the sum of ‘N’ over all test cases does not exceed 10^5.

# Time Limit: 1 sec
# Sample Input-1
# 2
# 3 
# 1 3 5 -1 
# 2 4 6 -1
# 1 
# 3 -1
# 6 -1
# Sample Output-1
# 1 2 3 4 5 6
# 3 6
# Explanation for Sample Input 1:
# For test case 1: 
#     It is explained above.
# For test case 2: 
#     We added the first element of the second LinkedList next to the first element of the first LinkedList. Hence the first LinkedList will look like 3 -> 6. 
# Sample Input -2
# 2
# 3 
# 1 2 3 -1
# -5 -2 -3 -1
# 3 
# 24 42 13 -1
# 91 42 13 -1
# Sample Output -2
# 1 -5 2 -2 3 -3
# 24 91 42 42 13 13

from os import *
from sys import *
from collections import *
from math import *


# Following is the linked list node structure:

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

from typing import *

def build_linked(values : List) -> Optional[Node]:
    if not values or values[0] == -1:
        return None

    head = Node(int(values[0]))
    current = head
    for val in values[1:]:
        if val == -1:
            break
        current.next = Node(int(val))
        current = current.next
    return head
def merge(heads: List[Node]) -> None:
    # Write your code here.
    head1 = heads[0]
    head2 = heads[1]

    if not head1:
        return head2

    if not head2:
        return head1

    curr1, curr2 = head1, head2

    while curr1 and curr2:

        next1 = curr1.next
        next2 = curr2.next

        curr1.next = curr2
        curr2.next = next1

        curr1 = next1
        curr2 = next2

    return head1
    

