# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        def traverse_and_invert(node):
            temp_left = node.left
            temp_right = node.right
            node.right = temp_left
            node.left = temp_right
            if node.left is not None:
                traverse_and_invert(node.left)
            if node.right is not None:
                traverse_and_invert(node.right)

        traverse_and_invert(root)
        return root
