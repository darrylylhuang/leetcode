class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find slow/fast collision that is (C - r) away from the start of the cycle
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # r = T = tail length
        slow = 0
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]

        # return the duplicate number
        return nums[slow]
