# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def sameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p and q and p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        else:
            return False  

    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.sameTree(root, subRoot):
            return True
        elif root is None:
            return False
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        