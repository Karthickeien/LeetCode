class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        ans = 0
        for c in count.values():
            if c < 2:
                return -1
            ans += (c + 2) // 3
        return ans
