class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < len(s) and j > -1:
            # search right from start for alphanum
            while i < len(s) - 1 and not s[i].isalnum():
                i += 1
            # search left from end for alphanum
            while j > 0 and not s[j].isalnum():
                j -= 1

            # two alphanums found; compare
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
