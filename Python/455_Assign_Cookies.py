class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi = 0
        sj = 0 
        res = 0
        while gi < len(g) and sj < len(s):
            if s[sj] >= g[gi]:
                gi += 1
                sj += 1
                res += 1
            else:
                sj += 1
        return res
            