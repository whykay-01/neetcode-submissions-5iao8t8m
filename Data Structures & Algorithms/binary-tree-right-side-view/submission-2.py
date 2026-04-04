# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrderTraversal(self, root: Optional[TreeNode]) -> List[int]: 

        res = []

        def dfs_helper(root, depth):
            if not root:
                return None
            if len(res) == depth:
                res.append([])
            
            res[depth].append(root.val)
            dfs_helper(root.left, depth + 1)
            dfs_helper(root.right, depth + 1)
        
        dfs_helper(root, 0)
        return res
        

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        level_ordered_tree = self.levelOrderTraversal(root)
        res = []
        for level in level_ordered_tree:
            # print(level)
            res.append(level[-1])
        return res