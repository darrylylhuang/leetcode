# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.maxDepthR(root)

    def maxDepthR(self, root):
        """
        Find max depth recursively
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Null nodes are depth 0
        if not root:
            return 0
        # Check children's heights and add 1 for the current node
        else:
            return max(self.maxDepthR(root.left), self.maxDepthR(root.right)) + 1
