class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # O(NlogN) -> create a heap first
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            stone_x, stone_y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            
            if stone_y < stone_x:
                heapq.heappush_max(stones, stone_x - stone_y)
        
        if len(stones) == 0:
            # if the heap is empty -- return 0
            return 0

        return stones[0]
