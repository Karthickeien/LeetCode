class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [0] * len(nums)
        length = 0
        for num in nums:
            i = bisect.bisect_left(dp, num, 0, length)
            dp[i] = num
            if i == length:
                length += 1
        return length
