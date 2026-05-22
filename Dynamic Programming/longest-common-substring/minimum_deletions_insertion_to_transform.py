#Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters. Write a function to calculate the count of the minimum number of deletion and insertion operations.

#bottomUp
def minimumDeletionAndInsertion(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0] * (n1+1) for _ in range(n2+1)]

    for r in range(1, n2+1):
        for c in range(1, n1 + 1):
            if s1[r-1] == s2[c-1]:
                dp[r][c] = dp[r-1][c-1]
            else:
                dp[r][c] = max(dp[r-1][c], dp[r][c-1]) + 1
    
    return dp[n2][n1]