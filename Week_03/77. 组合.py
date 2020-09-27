class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        index = 0
        result = []
        comb = []
        self.dfs(n, k, result, comb, 0)
        return result

    
    def dfs(self, n, k, result, comb, index):
        if len(comb) == k: 
            result.append(comb[:])
            return
        for i in range(index,n):
           comb.append(i+1)
           self.dfs(n, k, result, comb, i+1)
           comb.pop()
