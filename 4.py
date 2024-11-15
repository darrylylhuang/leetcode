class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, r1 = 0, len(nums1) - 1
        l2, r2 = 0, len(nums2) - 1
        # pointers in different lists may move at different rates

        while l1 < r1 and l2 < r2:

            # move the lesser left pointer towards the "middle"
            if nums1[l1] < nums2[l2]:
                l1 = (l1 + r1) // 2
            else:
                l2 = (l2 + r2) // 2

            # move the greater right pointer towards the "middle"
            if nums1[r1] < nums2[r2]:
                r2 = (l2 + r2) // 2
            else:
                r1 = (l1 + r1) // 2
