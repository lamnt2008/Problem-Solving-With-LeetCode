#Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.



def LengthOfmaximumSumIncreasingSubLIS(nums):
    n = len(nums)
    if n < 1:
        return n
    dp = [num for num in nums]
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + nums[i])
    return max(dp)





##top down with memoization
class Solution:
  def findMSIS(self, nums):
    dp = {}
    return self.findMSISRecursive(dp, nums, 0, -1, 0)


  def findMSISRecursive(self, dp, nums, currentIndex,  previousIndex,  sum):
    if currentIndex == len(nums):
      return sum

    subProblemKey = str(currentIndex) + "-" + \
                    str(previousIndex) + "-" + str(sum)

    if subProblemKey not in dp:
      # include nums[currentIndex] if it is larger than the last included number
      s1 = sum
      if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
        s1 = self.findMSISRecursive(
          dp, nums, currentIndex + 1, currentIndex, sum + nums[currentIndex])

      # excluding the number at currentIndex
      s2 = self.findMSISRecursive(
        dp, nums, currentIndex + 1, previousIndex, sum)
      dp[subProblemKey] = max(s1, s2)

    return dp.get(subProblemKey)


def main():
  sol = Solution()
  print(sol.findMSIS([4, 1, 2, 6, 10, 1, 12]))
  print(sol.findMSIS([-4, 10, 3, 7, 15]))


main()
