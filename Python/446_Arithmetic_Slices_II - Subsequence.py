class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        map = [defaultdict(int) for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff <= -2147483648 or diff > 2147483647:
                    continue
                d = diff
                c1 = map[i][d]
                c2 = map[j][d]
                res += c2
                map[i][d] = c1 + c2 + 1
        return res