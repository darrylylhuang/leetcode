class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = [1]
        # prefix products
        # placeholders in solution space
        # do not include the final element in the prefixes
        for i in range(len(nums) - 1):
            products.append(nums[i] * products[i])
        # postfix products
        # tracked as int
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # products[i] = prefix * postfix
            products[i] *= postfix
            postfix *= nums[i]
        return products
