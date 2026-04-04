from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def count_good_nodes(root, max_val = -101, count = 0):

            if not root:
                return 0
            count = 0
            if root.val >= max_val:
                count = 1

            updated_max_val = max(root.val, max_val)
            count += count_good_nodes(root.left, updated_max_val)
            count += count_good_nodes(root.right, updated_max_val)
            return count
        
        return count_good_nodes(root)

