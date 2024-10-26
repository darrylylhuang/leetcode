class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while (i < j):
            # sum is too small, increment start
            while i < j and target > numbers[i] + numbers[j]:
                i += 1

            # sum is too large, decrement end
            while i < j and target < numbers[i] + numbers[j]:
                j -= 1

            # loop end means we've found a complement addend, or j has reached i
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
