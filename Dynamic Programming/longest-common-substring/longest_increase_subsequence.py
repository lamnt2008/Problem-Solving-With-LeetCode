#Given an integer array nums, return the length of the longest strictly increasing subsequence.

#Approach 1: Recursive
def LengthOfLIS(nums):
    n = len(nums)
    if n < 2:
        return n
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


#Approach 2:

def LengthOfLISWithRecursive(nums):
    memo = {}
    def solving(nums, curr, pre):
        if (curr, pre) in memo:
            return memo[(curr, pre)]
        if curr == len(nums):
            return 0
        c1 = 0
        if pre == -1 or  (curr < len(nums) and nums[curr] > nums[pre]):
            c1 = 1 + solving(nums, curr + 1, curr) 
        
        c2  = solving(nums, curr+1, pre)
        memo[(curr, pre)] = max(c1, c2)
        return max(c1,c2)

    return solving(nums, 0, -1)
