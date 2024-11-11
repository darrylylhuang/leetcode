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
            # check all our points of comparison to make sure we don't skip over them
            if target == nums[mid]:
                return mid
            elif target == nums[r]:
                return r
            elif target == nums[l]:
                return l
            # target can only be greater than r if the list has been rotated, so we search left
            elif target > nums[r]:
                # unless we're already in the "left sorted portion"
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            # there are a few cases to consider if target < r
            else:
                # if target < mid and we're in the "right sorted portion", we should search left
                # if target < mid and the list hasn't been rotated, we should also search left
                # in all other cases, we search right
                if target < nums[mid] and (nums[mid] < nums[l] or nums[l] < nums[r]):
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
