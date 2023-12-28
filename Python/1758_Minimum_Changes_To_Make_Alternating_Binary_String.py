class Solution:
    def minOperations(self, s: str) -> int:
        count_01, count_10 = 0, 0
        
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    count_01 += 1
                if s[i] != '1':
                    count_10 += 1
            else:
                if s[i] != '1':
                    count_01 += 1
                if s[i] != '0':
                    count_10 += 1
        
        return min(count_01, count_10)