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
            if i == len(s):
                break

            # search left from end for alphanum
            while j > -1 and not s[j].isalnum():
                j -= 1
            if j == -1:
                break

            # two alphanums found; compare
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
