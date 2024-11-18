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
        # return self.height_and_max_diameter(root)[1]
        return self.diameterOfBinaryTree2(root)

    def height_and_max_diameter(self, root):
        """
        Find height and max diameter recursively
        :type root: Optional[TreeNode]
        :rtype: (int, int)
        """
        # Null nodes are depth 0, and have diameter 0
        if not root:
            return (0, 0)
        # Check children's heights and add 1 for the current node
        else:
            (l_height, l_diameter) = self.height_and_max_diameter(root.left)
            (r_height, r_diameter) = self.height_and_max_diameter(root.right)
            height = max(l_height, r_height) + 1
            diameter = l_height + r_height
            max_diameter = max(diameter, l_diameter, r_diameter)
            return (height, max_diameter)

    def diameterOfBinaryTree2(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0

        def calculate_height_update_max_diameter(tree):
            """
            Returns height and updates max diameter
            """
            if not tree:
                return 0
            l = calculate_height_update_max_diameter(tree.left)
            r = calculate_height_update_max_diameter(tree.right)
            self.max_diameter = max(self.max_diameter, l + r)
            return max(l, r) + 1

        calculate_height_update_max_diameter(root)
        return self.max_diameter
