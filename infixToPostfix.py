# Problem statement
# You are given a string 'exp' which is a valid infix expression.



# Convert the given infix expression to postfix expression.



# Note:
# Infix notation is a method of writing mathematical expressions in which operators are placed between operands. 

# For example, "3 + 4" represents the addition of 3 and 4.

# Postfix notation is a method of writing mathematical expressions in which operators are placed after the operands. 

# For example, "3 4 +" represents the addition of 3 and 4.

# Expression contains digits, lower case English letters, ‘(’, ‘)’, ‘+’, ‘-’, ‘*’, ‘/’, ‘^’. 


# Example:
# Input: exp = ‘3+4*8’

# Output: 348*+

# Explanation:
# Here multiplication is performed first and then the addition operation. Hence postfix expression is  3 4 8 * +.


# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 3^(1+1)


# Expected Answer:
# 311+^


# Output printed on console:
# 311+^


# Explanation of Sample Input 1:
# For this testcase, we will evaluate 'b' = (1+1) first. 

# Hence it's equivalent postfix expression will be "11+". 

# Next we will evaluate 3^b. It's equivalent postfix expression will be "3b^". 

# Replacing 'b' with it's equivalent postfix we get "311+^".


# Sample Input 2:
# a+b+c+d-e


# Expected Answer:
# ab+c+d+e-


# Output printed on console:
# ab+c+d+e-


# Expected Time Complexity:
# Try to do this in O(n).


# Constraints:
# 1 <= 'n' <= 5000 

# ‘n’, is the length of EXP
# The expression contains digits, lower case English letters, ‘(’, ‘)’, ‘+’, ‘-’, ‘*’, ‘/’, ‘^’. 

# Time Limit: 1 sec

def infixToPostfix(exp: str) -> str:
    # Write your code here.
    def precedence(op):
        if op == "^":
            return 3
        elif op == "*" or op == "/":
            return 2
        elif op == "+" or op == "-":
            return 1
        return 0

    def is_right_associstive(op):
        return op == '^'

    stack = []
    result = []

    for char in exp:
        if char.isalnum():
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        else:
            while (stack and stack[-1] != '(' and (precedence(stack[-1])> precedence(char) or (precedence(stack[-1]) == precedence(char) and not is_right_associstive(stack[-1])))):
                result.append(stack.pop())

            stack.append(char)

    while stack:
        result.append(stack.pop())

    return ''.join(result)