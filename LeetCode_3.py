class Solution:
    def lengthOfLongestSubstring(self, s):
        last = {}          # char -> last index seen
        left = 0           # window left bound
        best = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                # jump left just past previous occurrence of ch
                left = last[ch] + 1
            last[ch] = right
            best = max(best, right - left + 1)

        return best


# Local testing
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(s.lengthOfLongestSubstring("bbbbb"))     # 1
    print(s.lengthOfLongestSubstring("pwwkew"))    # 3
    print(s.lengthOfLongestSubstring("abba"))      # 2
    print(s.lengthOfLongestSubstring("tmmzuxt"))   # 5


