#Given two strings 's1' and 's2', find the length of the longest subsequence which is common in both the strings. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

#Approach 1: Brute force by recursive

def LCSubsequence(s1, s2):

    def solving(s1, s2, i1, i2, count):
        if i1 == len(s1) or i2 == len(s2):
            return count
        
        if s1[i1] == s2[i2]:
            return 1 +  solving(s1, s2, i1+1, i2 + 1, count + 1)
        
        count1 = solving(s1, s2, i1 + 1, i2, count)
        count2 = solving(s1, s2, i1, i2 + 1, count)

        return max(count1, count2)


#Approach 2: Top down approach with memoiry

def LCSubsequenceWithTopDownDP(s1, s2):
    memo = {}
    def solve(s1, s2, i1, i2, count):
        if i1 == len(s1) or i2 == len(s2):
            memo[(i1,i2)] = count
            return count
        
        if s1[i1] == s2[i2]:
            return 1 + solve(s1, s2, i1+1, i2+1, count+1)
        
        count1 = solve(s1, s2, i1+1, i2, count)
        count2 = solve(s1,s2, i1, i2 + 1, count)

        memo[(i1,i2)] = max(count1, count2)
        return memo[(i1,i2)]
    

#Approach 3: Bottom up approach 

def LCSubsequenceWithBottomUp(s1,s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0] * (n1+1) for _ in range(n2+1)]

    for r in range(1, 1+n2):
        for c in range(1, 1 + n1):
            if s1[r-1] == s2[c-1]:
                dp[r][c] = dp[r-1][c-1] + 1
            else:
                dp[r][c] = max(dp[r][c-1], dp[r-1][c-1])
        

    return dp[n2][n1]