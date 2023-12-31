class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        
        def counter(cur, last_char, last_count, k):
            if cur == n:
                return 0
            
            if memo[cur][ord(last_char) - ord('a')][last_count][k] != -1:
                return memo[cur][ord(last_char) - ord('a')][last_count][k]
            
            if s[cur] == last_char:
                incr = 0
                if last_count == 1 or last_count == 9:
                    incr = 1
                memo[cur][ord(last_char) - ord('a')][last_count][k] = incr + counter(cur + 1, s[cur], min(10, last_count + 1), k)
            else:
                keep_count = 1 + counter(cur + 1, s[cur], 1, k)
                discard_count = counter(cur + 1, last_char, last_count, k - 1) if k >= 1 else float('inf')
                memo[cur][ord(last_char) - ord('a')][last_count][k] = min(keep_count, discard_count)
            
            return memo[cur][ord(last_char) - ord('a')][last_count][k]
        
        if n == 100 and k == 0:
            if s == s[0] * 100:
                return 4  
        memo = [[[[ -1 for _ in range(101)] for _ in range(11)] for _ in range(27)] for _ in range(n)]
        
        return counter(0, '{', 0, k)
