class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        char_count = dict()
        for r in range(len(s)):
            if s[r] in char_count:
                s[r] += 1
            else:
                s[r] = 1
