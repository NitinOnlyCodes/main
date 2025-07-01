#sorting array with magic bits
# sort an array A using magic bits, where:
# the first and last elements of a subarray must have different magic bits
# rearrange the subarray elements
# find the minimum operations to sort the array or return-1 if impossible

def sort_magic_array(N, A, S):
    operations = 0
    sorted_A =sorted(A)
    
    if A == sorted_A:
        return operations
    
    for i in range(N):
        for j in range(i+1,N):
            if S[i]!=S[j]:
                A[i:j+1] = sorted(A[i:j+1])
                operations += 1
                if A== sorted_A:
                    return operations
    return -1

print(sort_magic_array(5,[1,3,2,3,7],"11010"))