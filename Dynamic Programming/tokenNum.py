# Probability of Token number correctness
# Given N token, each token can have two
# possible number (A[i] or B[i]) with a given
# probability P[i]
# find the probability that all tokens have distinct numbers

def token_numbering(N, P, A, B):
    probability = 1.0
    seen = set()

    for i in range(N):
        if A[i] not in seen:
            probability *= P[i]/100
            seen.add(A[i])
        elif B[i] not in seen:
            probability *= (100-P[i])/100
            seen.add(B[i])
        else:
            return 0.0
    return round(probability, 9)
print(token_numbering(2, [50,50],[1,2],[2,1]))