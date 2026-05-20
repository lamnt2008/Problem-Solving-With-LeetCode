#Given a set of positive numbers (non zero) and a target sum 'S'. Each number should be assigned either a '+' or '-' sign. We need to find out total ways to assign symbols to make the sum of numbers equal to target 'S'.

#Input: {1, 1, 2, 3}, S=1
# Output: 3
# Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

#brute force: find the subsets has sum equal (totalSum + target)/2

def findSignedTarget(nums, targetNum):
    ans = 0
    total = sum(nums)
    target = (total + targetNum) // 2
    def solve(currentIdx, sum1):
        nonlocal ans
        if currentIdx == len(nums):
            if sum1 == target:
                ans += 1 
        
            return
        
        solve(currentIdx+1, sum1+nums[currentIdx])
        solve(currentIdx+1, sum1 )
    solve(0, 0) 

# optimize
class Solution: 
  def findTargetSubsets(self, num, s):
    if any(i < 1 for i in num):
      return -1 #invalid input, the problem expects only positive numbers

    totalSum = sum(num)

    # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s +totalSum) / 2'
    if totalSum < s or (s + totalSum) % 2 == 1:
      return 0

    return self.countSubsets(num, int((s + totalSum) / 2))


  # this function is exactly similar to what we have in 'Count of Subset Sum' problem
  def countSubsets(self, num, sum):
    n = len(num)
    dp = [0 for x in range(sum+1)]
    dp[0] = 1

    # with only one number, we can form a subset only when the required sum is equal to the number
    for s in range(1, sum+1):
      dp[s] = 1 if num[0] == s else 0

    # process all subsets for all sums
    for i in range(1, n):
      for s in range(sum, -1, -1):
        if s >= num[i]:
          dp[s] += dp[s - num[i]]

    return dp[sum]

