# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.diameterOfBinaryTreeR(root)

    def diameterOfBinaryTreeR(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        max_diameter = 0
        # TODO: calculate intermediate height and diameter
        # diameter = left_height + right_height
        # max_diameter = max(left_diameter, right_diameter, diameter)

        # children may have larger sums than root if the tree is unbalanced
        return max(self.maxDepthR(root.left) + self.maxDepthR(root.right), self.diameterOfBinaryTreeR(root.left), self.diameterOfBinaryTreeR(root.right))

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
