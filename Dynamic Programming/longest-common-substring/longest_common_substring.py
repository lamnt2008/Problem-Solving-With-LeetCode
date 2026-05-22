#Given two strings 's1' and 's2', find the length of the longest substring which is common in both the strings.


#Approach1: Brute force by recursive
def findLCSLength( s1, s2):
    def solve(s1, s2, i1, i2, count):
        if i1 == len(s1) or i2 == len(s2):
            return count
        
        if s1[i1] == s2[i2]:
            count =  solve(s1, s2, i1+1, i2 + 1, count+1)
        
        count1 = solve(s1, s2, i1+1, i2, count)
        count2 = solve(s1, s2, i1, i2+1, count)

        return max(count1, count2, count)
    
    return solve(s1,s2,0,0, 0)


#Approach: top down dynamic with memoization
def findLCSLength(s1, s2):
    memo = {}
    def solve(s1, s2, i1, i2, count):
        if i1 == len(s1) or i2 == len(s2):
            return count
        if (i1,i2) in memo:
            return memo[(i1,i2)]
        if s1[i1] == s2[i2]:
            count =  solve(s1, s2, i1+1, i2 + 1, count+1)
        
        count1 = solve(s1, s2, i1+1, i2, count)
        count2 = solve(s1, s2, i1, i2+1, count)
        memo[(i1,i2)]= max(count1, count2, count)
        return memo[(i1,i2)]
    
    return solve(s1,s2,0,0, 0)


#Approach 3: Bottom up DP
def findLCSLength(s1, s2):
    dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]
    for r in range(1, len(s2)+1):
        for c in range(1, len(s1)+1):
            if s1[c-1] == s2[r-1]:
                dp[r][c] = dp[r-1][c-1] + 1
    
    return max(dp)
