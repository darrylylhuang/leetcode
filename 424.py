class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_length = 0
        l = 0
        char_count = dict()
        for r in range(len(s)):
            if s[r] in char_count:
                char_count[s[r]] += 1
            else:
                char_count[s[r]] = 1

            substring_length = r - l + 1
            # a valid substring of duplicate characters can be created by substituting k letters
            if substring_length - max(char_count.values()) <= k:
                # potentially update max length
                max_length = max(max_length, substring_length)
            else:
                # move the sliding window
                l += 1
                char_count[s[l]] -= 1
        return max_length
