"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # handle the edge case of an empty graph
        if not node:
            return None

        old_to_new = dict()
        
        def dfs(node):
            # if we already went through the node - simply return what we know
            if node in old_to_new:
                return old_to_new[node]
            
            # copy at its entirety and put in the mapping
            copy = Node(node.val)
            old_to_new[node] = copy

            # call recursion for all the neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            # return the final fully copied graph
            return copy
        
        # inititate the algo
        return dfs(node)
        
