class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_indices = {}
        max_length = -1

        for i, char in enumerate(s):
            if char not in char_indices:
                char_indices[char] = i
            else:
                max_length = max(max_length, i - char_indices[char] - 1)
        
        return max_length