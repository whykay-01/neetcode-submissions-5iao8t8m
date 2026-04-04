class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non decreasing allows for duplicates, and not just an increasing order of numbers
        l, r = 0, len(numbers) - 1

        while l < r:
            sum_of_two = numbers[l] + numbers[r] 
            
            if sum_of_two == target:
                return [l+1, r+1]

            elif sum_of_two < target:
                l += 1
            
            else:
                r -= 1