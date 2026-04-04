from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0
        q = deque()
        q.append([root, -101])

        while q:
            node, max_val = q.popleft()
            
            if node.val >= max_val:
                res += 1
            
            updated_max_val = max(max_val, node.val)

            if node.left:
                q.append([node.left, updated_max_val])
            
            if node.right:
                q.append([node.right, updated_max_val])
            
        return res


