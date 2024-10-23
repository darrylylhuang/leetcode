class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # con_lens stands for consecutive lengths
        con_lens = dict()
        for num in nums:
            # don't need to do anything if a num already exists
            if num not in con_lens:
                # new num - four cases:
                # 3. num - 1 exists AND num + 1 exists
                if num - 1 in con_lens and num + 1 in con_lens:
                    con_lens[num] = con_lens[num - 1] + con_lens[num + 1]
                    con_lens[num] += 1
                    con_lens[num - 1] = con_lens[num]
                    con_lens[num + 1] = con_lens[num]
                # 1. only num - 1 exists
                elif num - 1 in con_lens:
                    con_lens[num - 1] += 1
                    con_lens[num] = con_lens[num - 1]
                # 2. only num - 1 exists
                elif num + 1 in con_lens:
                    con_lens[num + 1] += 1
                    con_lens[num] = con_lens[num + 1]
                # 4. new num is an island
                else:
                    con_lens[num] = 1

        longest = 0
        for length in con_lens.values():
            if length > longest:
                longest = length

        return longest
