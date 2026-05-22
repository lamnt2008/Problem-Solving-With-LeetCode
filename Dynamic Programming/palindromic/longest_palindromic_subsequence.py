#Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence, elements read the same backward and forward. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

def findLPSLengthRecurive(st):

    def solve(st, startIndex, endIndex):
        if startIndex > endIndex:
            return 0
        if startIndex == endIndex:
            return 1

        if st[startIndex] == st[endIndex]:
            return 2 + solve(st, startIndex + 1, endIndex - 1)
        
        c1 = solve(st, startIndex + 1, endIndex)
        c2 = solve(st, startIndex, endIndex - 1)
        return max(c1, c2)
        
    
    return solve(st, 0, len(st) - 1)

#use memoization
memo = {}
def solveDPMemoization(st, startIndex, endIndex):
    if (startIndex, endIndex)  in memo:
        return memo[(startIndex, endIndex)]
    if startIndex > endIndex:
        return 0
    if startIndex == endIndex:
        return 1

    if st[startIndex] == st[endIndex]:
        return 2 + solveDPMemoization(st, startIndex + 1, endIndex - 1)
    
    c1 = solveDPMemoization(st, startIndex + 1, endIndex)
    c2 = solveDPMemoization(st, startIndex, endIndex - 1)
    memo[(startIndex, endIndex)] = max(c1, c2)
    return memo[(startIndex, endIndex)]

#use bottom up dp
def bottomUp(st):
    n = len(st)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
    
    for startIndex in range(n-1,-1,-1):
        for endIndex in range(startIndex+1, n):
            if st[startIndex] == st[endIndex]:
                dp[startIndex][endIndex] = 2 + dp[startIndex+1][endIndex-1]
            else:
                dp[startIndex][endIndex] = max(dp[startIndex+1][endIndex], dp[startIndex][endIndex-1])
    
    return dp[0][n-1]