# given N tasks
# each day you can complete the First & Last Task
# Points are earned using the formula
# A[i]*(K-j), where j is the day number
# for Days > K, points are Zero

def findMaxPoint(N, K, A):
    dp = [[0]*(K+1) for _ in range(N)]
    left = 0
    right = N-1

    max_points = 0
    for j in range(K):
        max_points = max(max_points, A[left]*(K-j), A[right]*(K-j))
        left += 1
        right -= 1
    return max_points
print(findMaxPoint(4,3,[45, 85, 67, 32]))