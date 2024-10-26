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
            # search for complement addend
            while i < j and not target - numbers[i] == numbers[j]:
                j -= 1

            # loop end means we've found a complement addend, or j has reached i
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

            # increment the start pointer and do the whole process again
            j = len(numbers) - 1
            i += 1
