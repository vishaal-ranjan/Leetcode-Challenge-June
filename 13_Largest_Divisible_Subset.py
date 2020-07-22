class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        
        ans = []
        nums.sort()
        dp = [1]*n
        maxval = 1
        
        for i in range(1, n):
            for j in range(i):
                if (nums[i]%nums[j] == 0) and (1 + dp[j] > dp[i]):
                    dp[i] = 1 + dp[j]
                    maxval = max(maxval, dp[i])
        
        prev = -1
        for i in range(n-1, -1, -1):
            if (dp[i] == maxval) and (prev%nums[i] == 0 or prev == -1):
                ans.append(nums[i])
                maxval -= 1
                prev = nums[i]
                
        return ans