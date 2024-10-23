class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        nums_set = set(nums)
        for num in nums:
            # this is the beginning of a sequence
            if num - 1 not in nums_set:
                curr = 1
                while (num + curr in nums_set):
                    curr += 1
                longest = max(curr, longest)

        return longest
