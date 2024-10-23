class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_sets = dict()
        for num in nums:
            if num in all_sets:
                all_sets[num].add(num)
                all_sets[num + 1] = all_sets[num]
                all_sets[num - 1] = all_sets[num]
            else:
                new_set = set()
                new_set.add(num)
                all_sets[num] = new_set
                all_sets[num + 1] = new_set
                all_sets[num - 1] = new_set

        largest_set = 0
        for s in all_sets.values():
            if len(s) > largest_set:
                largest_set = len(s)

        return largest_set
