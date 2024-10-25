class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True
