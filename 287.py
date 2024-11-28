class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^2)
        for i in range(len(nums)):
            slow, fast = i, i + 1
            while nums[slow] != nums[fast] and fast < len(nums) - 1:
                fast += 1

            # found fast match
            if nums[slow] == nums[fast]:
                return nums[slow]
            # no match for fixed slow
