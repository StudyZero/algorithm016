class Solution:
    def maxCoins(self, a: List[int]) -> int:
        a=[1]+a+[1]
        @lru_cache(None)
        def dfs(i,j):
            if i>=j-1:
                return 0
            res=0
            for k in range(i+1,j):
                res=max(res,a[i]*a[j]*a[k]+dfs(i,k)+dfs(k,j))
            return res
        return dfs(0,len(a)-1)
