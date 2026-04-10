class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        
        # Add all intervals that end before the new one starts
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            # Add all intervals that start after the new one ends
            elif interval[0] > newInterval[1]:
                result.append(interval)
            # Overlap case: merge
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        # Find where to insert the merged interval and insert it
        # (insert at the right position to maintain sorted order)
        for i, interval in enumerate(result):
            if interval[0] > newInterval[0]:
                result.insert(i, newInterval)
                return result
        
        result.append(newInterval)
        return result


