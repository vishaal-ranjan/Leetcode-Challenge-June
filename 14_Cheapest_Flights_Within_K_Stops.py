class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        self.mincost = 2**31 - 1
        self.reached = False
        flight_dict = {}
        
        for s,d,p in flights:
            if s in flight_dict:
                flight_dict[s].append((d,p))
            else:
                flight_dict[s] = [(d,p)]
                
        self.dfs(flight_dict, 0, src, dst, K)
        
        if not self.reached:
            return -1
        return self.mincost
        
    def dfs(self, flight_dict, cur_price, src, dst, K):
        if src in flight_dict:
            for d, p in flight_dict[src]:
                if d == dst:
                    self.reached = True
                    self.mincost = min(self.mincost, cur_price+p)
                    continue
                if K>0 and cur_price+p < self.mincost:
                    self.dfs(flight_dict, cur_price+p, d, dst, K-1)