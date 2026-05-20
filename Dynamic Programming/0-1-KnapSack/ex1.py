#Given two integer arrays to represent weights and profits of 'N' items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number 'C'. Write a function that returns the maximum profit. Each item can only be selected once, which means either we put an item in the knapsack or skip it.

#Solve by top down with memoization
class Solution:
    def solveKnapsackByTopDown(self, profits, weights, capacity):
        return self.knapsackRecursive(profits, weights, capacity, 0)

     
    def knapsackRecursive(self, profits, weights, capacity,     currentIndex):
        memory = {}
        if capacity in memory:
            return memory[capacity]
        if capacity <= 0 or currentIndex >= len(weights):
            return 0
        
        profit1 = 0

        if weights[currentIndex] <= capacity:
            profit1 = profits[currentIndex] +  self.knapsackRecursive(profits, weights, capacity - weights[currentIndex], currentIndex + 1)
        
        profit2 = self.knapsackRecursive(profits, weights, capacity, currentIndex + 1)
        memory[capacity] = max(profit1, profit2)
        return  memory[capacity]

    def solveByBottomUp(self, profits, weights, capacity):
        dp = [[0] * len(profits) for _ in range(capacity+1)] 
        for i in range(capacity+1):
          if i >= weights[0]:
            dp[i][0] = profits[0]
        
        for i in range(capacity+1):
          for j in range(1,len(profits)):
            profit1 = 0
            if weights[j] <= i:
              profit1 = dp[i-profits[j]][j-1] + profits[j]
            
            profit2 = dp[i][j-1]
            dp[i][j] = max(profit2, profit1)
        
        return dp[capacity][len(profits)-1]
    


  

sol = Solution()
print(sol.solveByBottomUp(profits=[3,4,5], weights= [3,2,1], capacity=3))




#Subset have equal target sum 
def canPartition(self, num, sum):
    n = len(num)
    dp = [[False for x in range(sum+1)] for y in range(n)]

    # populate the sum = 0 columns, as we can always form '0' sum with an empty set
    for i in range(0, n):
      dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for s in range(1, sum+1):
      dp[0][s] = True if num[0] == s else False

    # process all subsets for all sums
    for i in range(1, n):
      for s in range(1, sum+1):
        # if we can get the sum 's' without the number at index 'i'
        if dp[i - 1][s]:
          dp[i][s] = dp[i - 1][s]
        elif s >= num[i]:
          # else include the number to see if we can find a subset to get the remaining sum
          dp[i][s] = dp[i - 1][s - num[i]]

    # the bottom-right corner will have our answer.
    return dp[n - 1][sum]