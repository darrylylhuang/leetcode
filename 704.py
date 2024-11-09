class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        while len(nums) > 0:
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
        return -1
