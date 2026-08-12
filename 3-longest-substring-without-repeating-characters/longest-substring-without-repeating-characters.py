class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = set()
        left = 0
        longest = 0

        for right in range (len(s)):
            while s[right] in n:
                n.remove(s[left])
                left += 1

            n.add(s[right])

            lenght = right - left + 1
            longest = max(longest,lenght)
        return longest