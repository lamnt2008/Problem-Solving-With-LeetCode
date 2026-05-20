class Solution:
    def findMaxProfit(self, profit, weight, maxWeight):
        def solve(currentIdx, currW):
            if currentIdx == len(profit) or currW <= 0:
                return 0
            
            profit1= 0 
            if currW >= weight[currentIdx]:
                profit1 = profit[currentIdx] + solve(currentIdx, currW - weight[currentIdx])
            profit2 = solve(currentIdx+1, currW)

            return max(profit1, profit2)
        
        return solve(0, maxWeight)
    

class Solution:
  def solveKnapsack(self,profits, weights, capacity):
    n = len(profits)
    # base checks
    if capacity <= 0 or n == 0 or len(weights) != n:
      return 0

    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]

    # populate the capacity=0 columns
    for i in range(n):
      dp[i][0] = 0

    # process all sub-arrays for all capacities
    for i in range(n):
      for c in range(1, capacity+1):
        profit1, profit2 = 0, 0
        if weights[i] <= c:
          profit1 = profits[i] + dp[i][c - weights[i]]
        if i > 0:
          profit2 = dp[i - 1][c]
        dp[i][c] = profit1 if profit1 > profit2 else profit2

    # maximum profit will be in the bottom-right corner.
    return dp[n - 1][capacity]


def main():
  sol = Solution()
  print(sol.solveKnapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
  print(sol.solveKnapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()
