class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # offset for when we skip parts of the list
        offset = 0
        # list size cannot go below 1 when slicing
        while len(nums) > 1:
            # because the list is sorted, we'll begin checking at the middle
            mid = len(nums) // 2
            if nums[mid] == target:
                return mid + offset
            # check the lesser half of the list
            elif nums[mid] > target:
                nums = nums[:mid]
            # check the greater half of the list
            else:
                offset += mid
                nums = nums[mid:]

        # empty list means target never found
        if nums[0] == target:
            return offset
        return -1
