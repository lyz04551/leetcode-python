class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        max_len = 1
        right = 1
        while right < len(s):
            if s[right] not in s[left:right]:
                max_len = max(max_len,right-left+1)
                right+=1
            else:
                while s[right] in s[left:right]:
                    left+=1
                right+=1
        return max_len


print(Solution().lengthOfLongestSubstring("dvdf")) #3