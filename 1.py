class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        differences = {}
        for i in range(len(nums)):
            if target - nums[i] in differences:
                return [differences[target - nums[i]], i]
            differences[nums[i]] = i
