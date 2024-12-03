class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        seen = set()
        for i in range(len(s)):
            if s[i] in seen:
                # possibly new max length
                max_length = max(max_length, len(seen))
                # reset
                seen = set()
            seen.add(s[i])

        # final check (substring may run to the end of the string)
        max_length = max(max_length, len(seen))
        return max_length
