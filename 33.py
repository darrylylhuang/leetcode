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
            elif target == nums[l]:
                return l
            # target between mid and r sorted
            # or the list has been rotated so check right (the left of r)
            elif nums[mid] < target and target < nums[r] or target < nums[mid] and nums[r] < nums[mid]:
                l = mid + 1
            # target between l and mid sorted
            # or the list has been rotated and check left (the right of l)
            elif nums[l] < target and target < nums[mid] or target > nums[mid] and nums[r] > nums[mid]:
                r = mid - 1
            else:
                return -1
        return -1
