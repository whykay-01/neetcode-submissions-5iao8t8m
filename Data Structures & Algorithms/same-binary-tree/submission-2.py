from collections import deque

class Solution:

    def traverseTree(self, root: Optional[TreeNode]) -> List:
        if not root:
            return [None]
        
        q = deque([root])

        tree = []

        while q: 
            node = q.popleft()

            if node:
                tree.append(node.val)
            
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
            
            else:
                tree.append(None)
        
        return tree


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_flat = self.traverseTree(p)
        q_flat = self.traverseTree(q)

        return p_flat == q_flat