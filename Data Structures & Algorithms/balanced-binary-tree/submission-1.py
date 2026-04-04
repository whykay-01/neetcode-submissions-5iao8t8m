# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def heightOfTree(self, root: Optional[TreeNode]) -> int:
        
        if not root: 
            return 0
        
        left_height = self.heightOfTree(root.left)
        right_height = self.heightOfTree(root.right)

        return max(left_height, right_height) + 1
        

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        # BFS - compute heights for all the trees - O(n^2)
        from collections import deque 
        q = deque([root])

        while q: 
            node = q.popleft()

            left_subheight = self.heightOfTree(node.left)
            right_subheight = self.heightOfTree(node.right)

            if abs(right_subheight - left_subheight) > 1:
                return False
            
            if node.left: 
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return True
        