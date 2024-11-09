class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # list size cannot go below 1 when slicing
        while len(nums) > 1:
            # because the list is sorted, we'll begin checking at the middle
            mid = len(nums) // 2
            if nums[mid] == target:
                return mid
            # check the lesser half of the list
            elif nums[mid] > target:
                nums = nums[:mid]
            # check the greater half of the list
            else:
                nums = nums[mid:]

        # empty list means target never found
        if nums[0] == target:
            return 0
        return -1
