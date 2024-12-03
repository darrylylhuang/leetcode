class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.lengthOfLongestSubstringDict(s)

    def lengthOfLongestSubstringDict(self, s):
        """
        Uses a dictionary of indices to move the left pointer past the duplicate letter
        :type s: str
        :rtype: int
        """
        max_length = 0
        # initialize r = -1 for empty string
        l, r = 0, -1
        seen = dict()
        for r in range(len(s)):
            if s[r] in seen:
                # possibly new max length
                max_length = max(max_length, r - l)
                # move the start of the substring to just after the duplicate character
                # make sure not to move the left pointer backwards
                l = max(l, seen[s[r]] + 1)
            seen[s[r]] = r

        # final check (substring may run to the end of the string)
        # remember to move the right pointer forward
        max_length = max(max_length, r + 1 - l)
        return max_length

    def lengthOfLongestSubstringSet(self, s):
        """
        Uses a set and increments left pointer to remove letters up to the duplicate
        :type s: str
        :rtype: int
        """
        max_length = 0
        # maintain sliding window with left/right pointers
        l = 0
        # maintain characters seen to prevent duplicates
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                # increment left and remove letters from the set until we've reached the duplicate
                seen.remove(s[l])
                l += 1
            # index math, but we're counting characters: add 1
            max_length = max(max_length, r - l + 1)
            seen.add(s[r])

        return max_length
