class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs.sort(key=lambda x: x[1])
        
        dp = defaultdict(int)
        dp[0] = 0
        
        for job in jobs:
            val = job[2] + dp[max(filter(lambda x: x <= job[0], dp))]
            if val > dp[max(dp)]:
                dp[job[1]] = val
        
        return dp[max(dp)]