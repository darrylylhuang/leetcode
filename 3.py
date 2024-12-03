class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        l, r = 0, -1
        seen = dict()
        for r in range(len(s)):
            if s[r] in seen:
                # possibly new max length
                max_length = max(max_length, r - l)
                # move the start of the substring to just after the duplicate character
                l = seen[s[r]] + 1
            seen[s[r]] = r

        # final check (substring may run to the end of the string)
        # remember to move the right pointer forward
        max_length = max(max_length, r + 1 - l)
        return max_length
