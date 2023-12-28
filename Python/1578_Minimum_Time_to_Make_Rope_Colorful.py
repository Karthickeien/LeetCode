class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = -1
        minTime = 0

        for i in range(len(colors)):
            if prev == -1 or colors[prev] != colors[i]:
                prev = i
            else:
                if neededTime[prev] < neededTime[i]:
                    minTime += neededTime[prev]
                    prev = i
                else:
                    minTime += neededTime[i]

        return minTime
