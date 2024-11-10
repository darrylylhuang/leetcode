class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
             mid = (l + r) // 2
             if nums[mid + 1] < nums[mid]:
                 return nums[mid + 1]
             elif nums[mid - 1] > nums[mid]:
                 return nums[mid]
             else:
                 break