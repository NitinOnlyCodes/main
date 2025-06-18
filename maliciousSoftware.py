# Problem statement
# The computer network of the company NinjaWorks has been attacked by malware, causing damage to the computer systems. Ninja is the chief security officer(CSO) of NinjaWorks and is trying to reduce the damage caused by the malware.

# The computer network at NinjaWorks consists of ‘N’ computers represented as an ‘N’ x ‘N’ adjacency matrix ‘GRAPH’. GRAPH[i][j] = 1, denotes that ith computer is directly connected to the jth computer. Some computers ‘INFECTED’ are already infected by the malware. If two computers are connected, and one is infected, then both computers will be infected by the malware. The spread of malware will continue until no more computers are left to be infected.

# Ninja being the CSO of NinjaWorks, can remove exactly one computer from ‘INFECTED’. But Ninja is confused about which computer to remove. Can you help Ninja find such a computer whose removal would minimize the spread of malware? If multiple such nodes exist, return the node with the smallest index.

# For Example:

# You are given ‘N’ = 5, ‘GRAPH’ = [[1, 1, 1, 0, 0],[1, 1, 0, 0, 0],[1, 0, 1, 0, 0],[0, 0, 0, 1, 1],[0, 0, 1, 0, 0]], ‘M’ = 2 and ‘INFECTED’ = [2 ,4]. 

# If we remove computer number 2 from infected computers, we can prevent computers numbers 0 and 1 from getting infected. Then total infected computers will be 2(3 and 4).  If we remove computer number 4 from infected computers, we can prevent computer number 3 from getting infected. Then total infected computers will be 3(0, 1, and 2). Hence, it’s better to remove computer number 2 from infected computers.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 10
# 2 <= N <= 2000
# 1 <= M <= N
# 0 <= GRAPH[i][j] <= 1
# GRAPH[i][j] == GRAPH[j][i]
# GRAPH[i][i] = 1
# 0 <= INFECTED[i] < N
# INFECTED contains unique elements.

# Time Limit: 1 sec
# Sample Input 1:
# 2
# 5 2 
# 1 1 1 0 0 
# 1 1 0 0 0 
# 1 0 1 0 0 
# 0 0 0 1 1 
# 0 0 1 0 0 
# 2 4
# 4 1 
# 1 1 1 0
# 1 1 0 0
# 1 0 1 1
# 0 0 1 1 
# 1
# Sample Output 1:
# 2
# 1
# Explanation of Sample Input 1:
# For the first test case, the graph will look like this:

# If we remove computer number 2 from infected computers, we can prevent computers numbers 0 and 1 from getting infected. Then total infected computers will be 2(3 and 4).  If we remove computer number 4 from infected computers, we can prevent computer number 3 from getting infected. Then total infected computers will be 3(0, 1, and 2). Hence, it’s better to remove computer number 2 from infected computers.

# For the second test case, the graph will look like this:

# We can only remove computer number 1.
# Sample Input 2:
# 2
# 2 2
# 1 1
# 1 1
# 0 1
# 3 1
# 1 0 1
# 0 1 0
# 1 0 1
# 2
# Sample Output 2:
# 0 2

