class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = [nums[0]]
        # prefix products
        # placeholders in solution space
        for i in range(1, len(nums)):
            products.append(nums[i] * products[i - 1])
        # postfix products
        # tracked as int
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix = products[i-1]
            if i == 0:
                prefix = 1
            products[i] = prefix * postfix
            postfix *= nums[i]
        return products
