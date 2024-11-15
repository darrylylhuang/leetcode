class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2
        # let A be the smaller array
        if len(A) > len(B):
            A, B = B, A
        l, r = 0, len(A) - 1
        mid = (l + r) // 2
        # subtract 1 twice since this is an index relating to A and B
        partition_point_B = half - mid - 2 

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

        # both lists bottomed out at the same time
        if l1 == r1 and l2 == r2:
            # m + n MUST be even so the median is an average
            return (nums1[l1] + nums2[l2]) / 2
        # nums2 bottomed out first
        elif l1 < r1:
            leftover = nums2[l1]
            while l1 < r1:
                if nums1[l1] < leftover:
                    l1 = (l1 + r1) // 2
                if nums1[r1] > leftover:
                    r1 = (l1 + r1) // 2
            if leftover > nums1[l1]:
                return float(leftover)
            else:
                return float(nums1[l1])
        # nums1 bottomed out first
        else:
            leftover = nums1[l2]
            while l2 < r2:
                if nums2[l2] < leftover:
                    l2 = (l2 + r2) // 2
                if nums1[r1] > leftover:
                    r2 = (l2 + r2) // 2
            if leftover > nums1[l2]:
                return float(leftover)
            else:
                return float(nums2[l2])
