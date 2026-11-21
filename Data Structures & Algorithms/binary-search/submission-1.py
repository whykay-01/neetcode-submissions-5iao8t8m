class Solution:

    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0:
            return -1

        mid = len(nums) // 2
        
        

        # found the element we were looking for: return the index of that element
        if nums[mid] == target:
            return mid
        
        # search recursively the right side of the array, cos target is larger than nums[mid]
        if target > nums[mid]:
            result = self.search(nums[mid+1:], target)
            return -1 if result == -1 else mid + 1 + result

        # search recursively the left side of the array, cos target is smaller than nums[mid]
        if target < nums[mid]:
            return self.search(nums[:mid], target)
        
        

        