# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1
        def traverse(node, depth):
            if node.left is None and node.right is None:
                return depth
            elif node.left is None:
                return traverse(node.right, depth + 1)
            elif node.right is None:
                return traverse(node.left, depth + 1)
            else:
                return max(traverse(node.left, depth + 1), traverse(node.right, depth + 1))
        return traverse(root, depth)