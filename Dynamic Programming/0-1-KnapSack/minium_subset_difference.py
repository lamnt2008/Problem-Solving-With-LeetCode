#Problem Statement Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.

class Solution:
    def canPartition(self, num):
        return self.canPartitionRecursive(num, 0, 0, 0)

    def canPartitionRecursive(self, num, currentIndex, sum1, sum2):
        if currentIndex == len(num):
            return abs(sum1 - sum2)
        
        diff1 = self.canPartitionRecursive(num, currentIndex + 1, sum1 + num[currentIndex], sum2)
        diff2 = self.canPartitionRecursive(num, currentIndex + 1, sum1 , sum2 + num[currentIndex])
        return min(diff1, diff2)
    

#top down dynamic programming with memoization

    def canPartitionRecursiveWithTopDown(self, num, currentIndex, sum1, memory):
        if currentIndex == len(num):
            return abs(sum(num) - 2 * sum1)

        if (currentIndex, sum1) in memory:
            print(currentIndex, sum1, "ss")
            return memory[(currentIndex, sum1)]
        
        sum1 = self.canPartitionRecursiveWithTopDown(num, currentIndex+1, sum1 + num[currentIndex], memory)
        sum2 = self.canPartitionRecursiveWithTopDown(num, currentIndex+1, sum1, memory)
        memory[(currentIndex, sum1)] = min(sum1, sum2)
        return memory[(currentIndex, sum1)]
    
    def minimum_subset_sum_difference(self, nums):
        total = sum(nums)
        n = len(nums)
        memo = {}

        def solve(index, sum1):
            # Nếu đã xét hết số
            if index == n:
                sum2 = total - sum1
                return abs(sum1 - sum2)

            # Nếu trạng thái này đã tính rồi
            if (index, sum1) in memo:
                return memo[(index, sum1)]

            # Cách 1: cho nums[index] vào nhóm A
            put_in_A = solve(index + 1, sum1 + nums[index])

            # Cách 2: cho nums[index] vào nhóm B
            put_in_B = solve(index + 1, sum1)

            # Lấy cách tốt hơn
            memo[(index, sum1)] = min(put_in_A, put_in_B)

            return memo[(index, sum1)]

        return solve(0, 0)
    

sol = Solution()
print(sol.minimum_subset_sum_difference([2,3,4]))