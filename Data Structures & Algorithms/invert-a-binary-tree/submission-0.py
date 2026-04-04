from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swap_children(self, node: TreeNode) -> None: 
        
        if node.left and node.right:
            node.left, node.right = node.right, node.left
        
        elif node.left and not node.right:
            node.right= node.left
            node.left = None

        elif node.right and not node.left:
            node.left = node.right
            node.right = None
        

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        queue = deque([root])
        while queue:

            node_to_process = queue.popleft()

            self.swap_children(node_to_process)

            if node_to_process.left:
                queue.append(node_to_process.left)

            if node_to_process.right:
                queue.append(node_to_process.right)
        
        return root