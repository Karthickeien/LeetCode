class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if d > n:
            return -1
        
        memo = [[-1] * n for _ in range(d + 1)]
        
        return self.dfs(d, 0, jobDifficulty, memo)
    
    def dfs(self, day, index, jobs, memo):
        n = len(jobs)
        if day == 0 and index == n:
            return 0
        if day == 0 or index == n:
            return float('inf')
        
        if memo[day][index] != -1:
            return memo[day][index]
        
        curMax = jobs[index]
        min_val = float('inf')
        for i in range(index, n):
            curMax = max(jobs[i], curMax)
            temp = self.dfs(day - 1, i + 1, jobs, memo)
            if temp != float('inf'):
                min_val = min(min_val, temp + curMax)
        
        memo[day][index] = min_val
        
        return min_val
