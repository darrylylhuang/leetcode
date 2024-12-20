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
        return self.maxDepthI_DFS(root)

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

    def maxDepthI_BFS(self, root):
        """
        Iteratively uses BFS to find max depth
        Level order traversal means that height = # of levels
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # empty trees are height 0
        if not root:
            return 0

        # initialize queue with root and height 0
        queue = [root]
        height = 0
        while queue:
            # pop all nodes on a single level
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            # increment height by # of levels
            height += 1
        return height

    def maxDepthI_DFS(self, root):
        """
        Iteratively uses pre-order DFS to find max depth
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # initialize stack with depth 1
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            curr, depth = stack.pop()
            # increase depth for non-null nodes, and add their children
            if curr:
                max_depth = max(max_depth, depth)
                stack.append((curr.left, depth + 1))
                stack.append((curr.right, depth + 1))
        return max_depth
