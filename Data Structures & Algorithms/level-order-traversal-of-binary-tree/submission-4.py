# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        def dfs_helper(root, depth):
            if not root:
                return
            if len(res) == depth:
                res.append([])
            
            dfs_helper(root.left, depth + 1)
            dfs_helper(root.right, depth + 1)
            res[depth].append(root.val)

        dfs_helper(root, 0)
        return res


        