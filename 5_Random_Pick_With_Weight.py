class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        self.total = 0
        for weight in w:
            self.total += weight
            self.prefix_sum.append(self.total)
        
    def pickIndex(self) -> int:
        rand = self.total*random.random()
        lo, hi = 0, len(self.prefix_sum)
        
        while lo < hi:
            mid = lo + (hi-lo)//2
            if rand > self.prefix_sum[mid]:
                lo = mid+1
            else:
                hi = mid
        return lo

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()