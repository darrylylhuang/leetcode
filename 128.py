class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_sets = dict()
        for num in nums:
            if num in all_sets:
                # num exists - three cases:
                # 3. num - 1 exists AND num + 1 exists
                if num - 1 in all_sets and num + 1 in all_sets:
                    all_sets[num] = all_sets[num - 1].union(all_sets[num + 1])
                    all_sets[num].add(num)
                    # update the other two sets
                # cases 1 and 2, num was added by one of its neighbours
                else:
                    all_sets[num].add(num)
                # in all cases, update the surrounding sets
                all_sets[num - 1] = all_sets[num]
                all_sets[num + 1] = all_sets[num]
            else:
                # num DNE which means adjacent numbers do not exist
                new_set = {num}
                all_sets[num] = new_set
                all_sets[num + 1] = new_set
                all_sets[num - 1] = new_set

        largest_set = 0
        for s in all_sets.values():
            if len(s) > largest_set:
                largest_set = len(s)

        return largest_set
