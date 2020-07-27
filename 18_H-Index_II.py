class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        lo, hi = 0, n - 1
        
        while lo <= hi:
            mid = (lo+hi)//2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] < n - mid:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return n - lo