#Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number 'S'.

class Solution:
    def countSubsets(self, num, sum1):
        dp = [[0] * len(num) for _ in range(sum1 + 1)]

        for i in num:
            dp[0][i] = 1
        
        for s in range(1, sum1 + 1):
            if num[0] == s:
                dp[0][s] = 1
        
        for s in range(1, sum1 + 1):
            for i in range(1, len(num)):
                dp[s][i] = dp[s][i-1]
                if s >= num[i]:
                    dp[s][i] += dp[s-num[i]][i-1]
        
        return dp[sum1][len(num)]
