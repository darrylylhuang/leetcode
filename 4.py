class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, r1 = 0, len(nums1) - 1
        l2, r2 = 0, len(nums2) - 1
