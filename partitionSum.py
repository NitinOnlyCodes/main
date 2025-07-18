#partition a set into tow subsets of equal sum

#input arr[] = [1, 5, 11, 5]
#output : true
#explaination: The array can be partitioned as [1, 5, 5] and [11]

#Using bottom-up appraoch to solve the question

def equalPartition(arr):
    arrSum = sum(arr)
    n = len(arr)

    if arrSum % 2 != 0:
        return False
    
    arrSum = arrSum // 2

    dp = [[False] * (arrSum + 1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for j in range(n+1):
        dp[i][0]=True

    for i in range(1, n+1):
        for j in range(1, arrSum+1):
            if j<arr[i-1]:

                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    return dp[n][arrSum]

if __name__=="__main__":
    arr = [1,5,11,5]
    if equalPartition(arr):
        print("True")
    else:
        print("False")