class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        # base case len(nums) == 2
        while l < r:
            mid = (l + r) // 2
            # max edge
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            # min edge
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            # mid < r means lesser value numbers exist to the left
            elif nums[mid] < nums[r]:
                r = mid - 1
            # mid > r means we are in a rotated portion of the array and a minimum value exists to the right
            else:
                l = mid + 1
                # mid == r should be impossible because of unique elements in input
        # only one element in the list
        return nums[0]
