class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # p for palindrome
        p = ""
        for i in range(len(s)):
            # strip non-alphanumeric characters
            if s[i].isalnum():
                # convert to lowercase
                p += s[i].lower()

        # begin algorithm
        for i in range(len(p)):
            if p[i] != p[len(p) - 1 - i]:
                return False
        return True
