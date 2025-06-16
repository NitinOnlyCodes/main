#room password combination using DP

# Problem description

# Gary has N houses, each with K rooms.
# Every room has a password from 1 to K.
# Given N, K, and a target capacity C,
# Find the number of ways to choose password
# such that their sum is equals C

# define dp[i][j] as the number of ways to achieve sum j using i houses
# integrate through possible rooms and update values accordingly

def count_password(N, K, C):
    dp = [[0] * (C+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        for j in range(C+1):
            for password in range(1, K+1):
                if j>= password:
                    dp[i][j] += dp[i-1][j-password]
    return dp[N][C]
print(count_password(3,4,5))