class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = []
        while len(strs) > 1:
           break
        return grouped_anagrams

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}
        for letter in s:
            if letter in s_count:
                s_count[letter] += 1
            else:
                s_count[letter] = 0
        for letter in t:
            if letter in t_count:
                t_count[letter] += 1
            else:
                t_count[letter] = 0
        return s_count == t_count