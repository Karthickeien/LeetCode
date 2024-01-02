class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        count = [0] * (len(nums) + 1)

        for num in nums:
            if count[num] + 1 > len(ans):
                ans.append([])
            count[num] += 1
            ans[count[num] - 1].append(num)

        return ans