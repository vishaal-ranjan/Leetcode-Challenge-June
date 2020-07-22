class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = collections.Counter(nums)
        
        for i in range(len(nums)):
            if d[0] != 0:
                nums[i] = 0
                d[0] -= 1
            elif d[1] != 0:
                nums[i] = 1
                d[1] -= 1
            else:
                nums[i] = 2