class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        for i in range(len(nums)):
            twoSum = self.twoSum(nums, -1 * nums[i])
            if twoSum != []:
                solution.append([nums[i], nums[twoSum[0]], nums[twoSum[1]]])
        return solution

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
        return []
