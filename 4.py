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

        neg_inf = float("-infinity")
        inf = float("infinity")
        # binary search to find suitable partition for A and B
        # an equal partition allows us to find the median
        while True:
            A_mid = (l + r) // 2
            # subtract 1 twice since this is an index AND A_mid is an index
            # while half is the number of elements we desire in the left partition
            B_mid = half - A_mid - 2

            A_left_max = A[A_mid] if A_mid >= 0 else neg_inf
            A_right_min = A[A_mid + 1] if (A_mid + 1) < len(A) else inf
            B_left_max = B[B_mid] if B_mid >= 0 else neg_inf
            B_right_min = B[B_mid + 1] if (B_mid + 1) < len(B) else inf

            # we included too many elements from A
            if A_left_max > B_right_min:
                r = A_mid - 1
            # we included too many elements from B (so we pad with A elements)
            elif B_left_max > A_right_min:
                l = A_mid + 1
            # suitable partition
            else:
                # odd elements
                if total % 2:
                    # partition is made right heavy since we round down with integer divison
                    return min(A_right_min, B_right_min)
                # even elements
                else:
                    return (max(A_left_max, B_left_max) + min(A_right_min, B_right_min)) / 2
