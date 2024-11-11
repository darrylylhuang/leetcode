class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        # base case len(nums) == 2
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target == nums[r]:
                return r
            # target between mid and r sorted
            # hope the list has been rotated and check right
            elif target > nums[mid] and target < nums[r] or target < nums[mid] and target > nums[r]:
                l = mid + 1
            # target between l and mid sorted
            # hope the list has been rotated and check left
            elif target < nums[mid] and target > nums[r] or target > nums[mid] and target < nums[r]:
                r = mid - 1
            else:
                return -1
        return -1
