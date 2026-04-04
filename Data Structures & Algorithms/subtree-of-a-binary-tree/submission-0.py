# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: 
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # do BFS for the root
        if not subRoot:
            return True
        
        q = deque([root])
        while q:
            node = q.popleft()
            value = self.isSameTree(node, subRoot)
            if value == True:
                return True
            else:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return False