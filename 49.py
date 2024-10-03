# Anagram Groups

class Solution(object):
    # Complexity is O(n^2) because it's possible for there to be 0 anagram pairs
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grouped_anagrams = []
        # loop through every string in the list
        for i in range(len(strs)):
            # Base Case, i = 0
            # there are no groups
            # therefore found == False
            # and the first group is added
            found = False
            for group in grouped_anagrams:
                if self.isAnagram(strs[i], group[0]):
                    # current string has found a group of anagram equivalents
                    found = True
                    group.append(strs[i])
            # create a new group of anagrams
            if not found:
                grouped_anagrams.append([strs[i]])
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
