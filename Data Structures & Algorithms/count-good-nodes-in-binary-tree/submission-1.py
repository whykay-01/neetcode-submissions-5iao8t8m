class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def count_good_nodes(root, max_so_far=-101):
            # hit rock bottom :) 
            if not root:
                return 0

            count = 0
            if root.val >= max_so_far:
                max_so_far = root.val
                count = 1
            
            count += count_good_nodes(root.left, max_so_far)
            count += count_good_nodes(root.right, max_so_far)
            return count
        
        return count_good_nodes(root)