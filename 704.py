class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # two pointers to metaphorically make the list smaller
        l, r = 0, len(nums) - 1
        # list size cannot go below 1 when slicing
        while l <= r:
            # because the list is sorted, we'll begin checking at the middle
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            # check the lesser half of the list
            elif nums[mid] < target:
                l = mid + 1
            # check the greater half of the list
            else:
                return mid
        return -1
