# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    # def flattenTree(self, root: TreeNode) -> List:

    #     q = deque([root])
    #     tree = []
    #     while q: 

    #         node = q.popleft()
    #         if not node:
    #             tree.append(None)
            
    #         else:
    #             tree.append(node)
            
    #         if node.left:
    #             q.append(node.left)
                
    #         if node.right:
    #             q.append(node.right)
        
    #     return tree
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or not p or not q:
            return
        
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)

        else:
            return root

        