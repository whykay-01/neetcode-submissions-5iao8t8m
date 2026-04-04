# two solutions
import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        

        heap = [(count, value) for value, count in freq.items()]
        heapq.heapify_max(heap)
        

        result = []
        for _ in range(k):
            count, value = heapq.heappop_max(heap)
            result.append(value)
        
        return result
        