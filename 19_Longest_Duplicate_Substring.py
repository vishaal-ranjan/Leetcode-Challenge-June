class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        a = 26
        mod = 2**40
        
        l, r = 0, n
        
        while l <= r:
            mid = l + (r-l)//2
            if self.search(mid, a, mod, n, nums) != -1:
                l = mid+1
            else:
                r = mid-1
        
        start = self.search(l-1, a, mod, n, nums)
        return S[start : start+l-1]
    
    def search(self, mid, a, mod, n, nums):
        # hash function
        h = 0
        for i in range(mid):
            h = (h*a + nums[i])%mod
        seen = {h}
        
        aL = pow(a, mid, mod)
        
        for start in range(1, n-mid+1):
            h = (h*a - nums[start-1]*aL + nums[start+mid-1])%mod
            if h in seen:
                return start
            seen.add(h)
        
        return -1