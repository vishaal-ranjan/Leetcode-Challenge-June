class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        count = 0
        for _ in range(32):
            if n&1:
                count += 1
            n = n>>1
        return True if count == 1 else False