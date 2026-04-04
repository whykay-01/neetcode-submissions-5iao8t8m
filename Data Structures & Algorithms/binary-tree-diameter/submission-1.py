# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def heightOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root: 
            # return 0 # or -1 
            return 0

        left_height = self.heightOfBinaryTree(root.left)
        right_height = self.heightOfBinaryTree(root.right)
        
        return max(left_height, right_height) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root: 
            return 0
        
        max_diameters = []
        q = deque([root])

        while q: 
            node = q.popleft()
            left_h = self.heightOfBinaryTree(node.left)
            right_h = self.heightOfBinaryTree(node.right)
            max_diameters.append(left_h + right_h)
            
            if node.left:
                q.append(node.left)
            if node.right: 
                q.append(node.right)

        return max(max_diameters)
