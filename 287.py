class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        slow, fast = 0, 1
        while nums[slow % n] != nums[fast % n]:
            slow += 1
            fast += 2
        return nums[slow % n]
