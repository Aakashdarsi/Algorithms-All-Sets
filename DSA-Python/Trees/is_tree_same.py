#https://leetcode.com/problems/same-tree/
# the tree is same when all are matching we can use any traversing technique. i have tried preorder . checking root is equal and then chencking wheteher left subtree is equal and checking whether right subtree is equal 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is not None and q is not None and p.val == q.val:
            l = self.isSameTree(p.left,q.left)
            r = self.isSameTree(p.right,q.right)
            if l and r: 
                return True
        return False