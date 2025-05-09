# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n < 2:
#             return s
        
#         max_len = 1
#         begin = 0
#         # dp[i][j] 表示 s[i..j] 是否是回文串
#         dp = [[False] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = True
        
#         # 递推开始
#         # 先枚举子串长度
#         for L in range(2, n + 1):
#             # 枚举左边界，左边界的上限设置可以宽松一些
#             for i in range(n):
#                 # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
#                 j = L + i - 1
#                 # 如果右边界越界，就可以退出当前循环
#                 if j >= n:
#                     break
                    
#                 if s[i] != s[j]:
#                     dp[i][j] = False 
#                 else:
#                     if j - i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
                
#                 # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
#                 if dp[i][j] and j - i + 1 > max_len:
#                     max_len = j - i + 1
#                     begin = i
#         return s[begin:begin + max_len]




class Solution:
    def longestPalindrome(self, s: str) -> str:
         # 首先检查输入的字符串是否为空，如果为空则直接返回空字符串
        if s == '':
            return ''
        n = len(s)
        start = end = 0
        for i in range(n):
             # 处理奇数长度的回文子串
            left = right = i    #以 s[i] 为中心，向两边扩展，直至左右字符不相等。
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            cur_len = right - left - 1
            if cur_len > end - start + 1:
                start = left + 1
                end = right - 1
            
            # 处理偶数长度的回文子串
            left, right = i, i+1    #以 s[i] 和 s[i+1] 为中心，向两边扩展，直至左右字符不相等。
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            cur_len = right - left - 1
            if cur_len > end - start + 1:
                start = left + 1
                end = right - 1
        return s[start:end+1]

