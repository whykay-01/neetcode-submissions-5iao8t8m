class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []

        def dfs(i, cur, total):
            # the subset has grown to it's max size -> add it to the result and return
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res