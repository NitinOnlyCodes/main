
# Problem statement
# John, a research scholar / Professor / Puzzle solver wants your help in publishing his work on SudoKube on his online blog for his followers and students.

# A SudoKube is a mixture of Rubics cube and Sudoku. A SudoKube has exactly 6 appearances of every digit from 1 to 9 across the cube, whereas Rubics cube has 6 different colours.

# As John wants to publish his work in text /document form (no video) he's concerned about how he would depict the step-by-step work of rotation in 2D form. Following are the notions and concepts John follows:

# 1) The six faces of the cube are named FRONT, BACK, UP, DOWN, LEFT, and RIGHT respectively.

# 2) Just like a Rubics cube which moves in 90 and 180 degrees in both clockwise and anti-clockwise directions, so can the SudoKube.

# 3) Any given face of the cube is a 3x3 square matrix whose indices are denoted by (0,0) to (2,2). The diagram below illustrates the same.

# 4) An elementary move is denoted in the following fashion:

# • If a given face is rotated 90 degrees clockwise about the axis passing from the center of the face to the center of the cube, the move is denoted by the first letter of the name of the face.

# • If the rotation is anticlockwise by 90 degrees, the letter is followed by an apostrophe (').

# • If the rotation is by 180 degrees, the letter is followed by a 2.


# The above image displays the position of the faces


# Above diagram displays the indices of the matrix on the faces

# John wants to test his notations on you. He has given you the initial position of the SudoKube and he has given you a set of operations to be performed on the SudoKube basis of his notation. After applying all the operations, the final SudoKube state should be the same as what John expects. Your task is to apply the operations and print the final SudoKube state.

# EXAMPLE :
# Refer to the Sample Input 1 explanation for a better understanding of the operations.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# ‘T' = 1
# Values in SudoKube will be between 1 and 9
# 1 <= Operations to be performed (‘Q’) <= 20
# Time Limit: 1 sec
# Sample Input 1 :
# 1
# 4 7 1
# 2 8 7
# 6 3 5
# 5 8 3
# 3 1 6
# 9 4 2
# 5 2 4
# 3 7 8
# 5 1 9
# 6 1 4
# 9 4 8
# 2 5 7
# 7 9 1
# 1 9 6
# 6 2 8
# 8 6 3
# 7 2 5
# 3 9 4
# 1
# F
# Sample Output 1 :
# 6 1 7
# 2 8 7
# 6 3 5
# 5 8 3
# 3 1 6
# 9 8 4
# 5 2 4
# 3 7 7
# 5 1 1
# 2 9 6
# 5 4 1
# 7 8 4
# 9 9 1
# 4 9 6
# 2 2 8
# 8 6 3
# 7 2 5
# 3 9 4
# Explanation Of Sample Input 1 :
# The Upper Face’s last row after rotation is copied to the first column of the Right Face
# The Right Face’s first column after rotation is copied to the first row of the Down Face
# The Down Face’s first row after rotation is copied to the last column of the Left Face
# The Left Face’s last column after rotation is copied to the last row of the Upper Face.
# Similarly, the Front Face is rotated 90 degrees clockwise.

# Sample Input 2 :
# 1
# 4 7 1
# 2 8 7
# 6 3 5
# 5 8 3
# 3 1 6
# 9 4 2
# 5 2 4
# 3 7 8
# 5 1 9
# 6 1 4
# 9 4 8
# 2 5 7
# 8 6 3
# 7 2 5
# 3 9 4
# 7 9 1
# 1 9 6
# 6 2 8
# 6
# F F F2 L L’ B
# Sample Output 2 :
# 4 7 1
# 2 8 7
# 5 3 5
# 3 5 4
# 3 1 6
# 9 4 2
# 3 2 4
# 8 7 8
# 5 1 9
# 6 1 4
# 9 4 8
# 2 5 7
# 8 6 5
# 7 2 3
# 3 9 6
# 6 1 7
# 2 9 9
# 8 6 1

