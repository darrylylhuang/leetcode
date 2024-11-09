class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # empty list means target never found
        if len(nums) == 0:
            return -1

        # because the list is sorted, we'll begin checking at the middle
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search(nums[:mid], target)
        else:
            return self.search(nums[mid:], target)
