class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_length = 0
        max_frequency = 0
        l = 0
        char_count = dict()
        for r in range(len(s)):
            if s[r] in char_count:
                char_count[s[r]] += 1
            else:
                char_count[s[r]] = 1
            max_frequency = max(max_frequency, char_count[s[r]])

            substring_length = r - l + 1
            # a valid substring of duplicate characters can be created by substituting k letters
            if substring_length - max_frequency <= k:
                # potentially update max length
                max_length = max(max_length, substring_length)
            else:
                # move the sliding window
                char_count[s[l]] -= 1
                l += 1
        return max_length
