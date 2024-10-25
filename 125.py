class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < len(s) and j >= 0:
            # search right from start for alphanum
            while not s[i].isalnum() and i < len(s):
                i += 1
            # search left from end for alphanum
            while not s[j].isalnum() and j >= 0:
                j -= 1
            # two alphanums found; compare
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
