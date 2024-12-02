class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        start = 0
        for i in range(1, len(s)):
            # duplicate letter
            if s[i] == s[i - 1]:
                # possibly new max length
                max_length = max(max_length, i - start)
                # move start of substring pointer
                start = i

        # final check (substring may run to the end of the string)
        max_length = max(max_length, i - start)
        return max_length
