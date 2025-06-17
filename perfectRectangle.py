# Problem statement
# You are given N rectangles whose sides are aligned with the x-axis and the y-axis. Each rectangle is represented by 4 integers [ a, b, c ,d ]. Here, (a, b) are x and y coordinates of the bottom left corner, and (c, d) are x and y coordinates of the top right corner.

# You need to find if they all together form a rectangular region cover.

# For Example :
# If the given rectangle is [1, 1, 3, 2]. It means the bottom left corner is at [1, 1] and the top right corner is at [3, 2]. Hence, the top left corner is at [1, 2] and the bottom right corner is at [3, 1].
# For the given figure is for N = 4, rectangle[0] = [1, 1, 4, 5], rectangle[1] = [4, 1, 6, 2], rectangle[3] = [4, 2, 6, 5], rectangle[4] = [6, 1, 8, 5].


# As they all form a big rectangle [1, 1, 8, 5]. So, the answer is 1.

# Note :

# Two integers are used to represent Point - x and y coordinates.

# Two points are used to represent a Rectangle - Bottom left corner and top right corner.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1<= T <= 50
# 1 <= N <= 20000
# 0 <=  'rectangle[i][j]' <= 20000
# rectangle[i].size = 4

# Where 'rectangle[i][j]'(0 <= j < 4)  denote the coordinates of the corners of the rectangle

# Time Limit: 1 sec
# Sample Input 1 :
# 2
# 3
# 3 1 4 4
# 1 1 3 3
# 1 3 3 4
# 3
# 3 1 4 4
# 1 1 3 3
# 1 3 4 4
# Sample Output 1 :
# 1
# 0 
# Explanation For Sample Input 1 :
# In the first test case, three rectangles are given - the first rectangle starts at (3, 1) and ends at (4, 4), the second rectangle starts at (1, 1) and ends at (3, 3), and the third rectangle starts at (1, 3) and ends at (3, 4). When these rectangles are combined, a big rectangle is formed starting at (1, 1) and it ends at (4, 4). So, the answer is 1.

# In the second test case, three rectangles are given - the first rectangle starts at (3, 1) and ends at (4, 4), the second rectangle starts at (1, 1) and ends at (3, 3), and the third rectangle starts at (1, 3) and ends at (4, 4). When these rectangles are combined, a big rectangle is formed starting at (1, 1) and ends at (4, 4) but the first and the third rectangles overlap into each other from (3, 3) to (4, 4). So, the answer is 0.
# Sample Input 2 :
# 2
# 4
# 1 3 2 4
# 3 1 4 2
# 3 2 4 4
# 1 1 2 3
# 5
# 1 3 2 4
# 3 1 4 2
# 3 2 4 4
# 1 1 2 3
# 2 1 3 4
# Sample Output 2 :
# 0
# 1

from os import *
from sys import *
from collections import *
from math import *

def perfectRectangle(rectangles):
    # Write your code here.
    # Return 0 or 1.
    if not rectangles:
        return 0

    x1 = float('inf')
    y1 = float('inf')
    x2 = float('-inf')
    y2 = float('-inf')

    area = 0
    points = defaultdict(int)

    for rect in rectangles:
        a, b, c, d = rect
        x1 = min(x1, a)
        y1 = min(y1, b)
        x2 = max(x2, c)
        y2 = max(y2, d)
        area += (c - a) * (d - b)

        points[(a, b)] ^= 1
        points[(a, d)] ^= 1
        points[(c, b)] ^= 1
        points[(c, d)] ^= 1

    if area != (x2 - x1) * (y2 - y1):
        return 0

    corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
    for corner in corners:
        if points.get(corner, 0) != 1:
            return 0
        del points[corner]

    for count in points.values():
        if count%2!=0:
            return 0

    return 1