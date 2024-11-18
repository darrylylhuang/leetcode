# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        return self.invertTreeR(root)

    def invertTreeR(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root

        # invert children
        self.invertTreeR(root.left)
        self.invertTreeR(root.right)

        # swap children so that this node is inverted
        placeholder = root.left
        root.left = root.right
        root.right = placeholder
        return root
