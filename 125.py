class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while True:
            # search right from start for alphanum
            while i < len(s) and not s[i].isalnum():
                i += 1
            # search left from end for alphanum
            while j >= 0 and not s[j].isalnum():
                j -= 1

            # stop the loop if we've gone out of bounds
            if i >= len(s):
                break
            if j < 0:
                break

            # two alphanums found; compare
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
