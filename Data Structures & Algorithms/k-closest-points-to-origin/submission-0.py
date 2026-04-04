class Solution:

    def distanceToZero(self, point: List[int]):
        x, y = point[0], point[1]

        return math.sqrt(
            x**2 + y**2
        )

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance_to_points_mapping = []

        for point in points:

            dist_to_zero = self.distanceToZero(point)
            distance_to_points_mapping.append((dist_to_zero, point)) 

        # now let's construct the min-heap based on the key of the distance_to_points_mapping
        heapq.heapify(distance_to_points_mapping)
        
        res = []
        while k >= 1:
            heap_top = heapq.heappop(distance_to_points_mapping)
            point_coordinates = heap_top[1]
            res.append(point_coordinates)
            k -= 1 
        
        return res
        
