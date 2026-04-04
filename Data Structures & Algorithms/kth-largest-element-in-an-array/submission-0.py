

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # res[0] --> largest
        # min(res) --> smallest element
        # if len(res) == k --> res[-1] is effectively the Kth largest element


        heapq.heapify_max(nums)

        for _ in range(k):
            item = heapq.heappop_max(nums)
        
        return item

