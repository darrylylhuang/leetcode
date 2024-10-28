class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        nums.sort()
        # fix a number -- nums[i]
        for i in range(len(nums)):
            # do a twoSum solution on the rest of the list
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    k -= 1
                if nums[j] + nums[k] < nums[i]:
                    j += 1
                if nums[j] + nums[k] == nums[i]:
                    solution.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
