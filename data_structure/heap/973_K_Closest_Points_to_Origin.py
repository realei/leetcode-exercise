"""
Day 5(Week of Heap):
#973. K Closest Points to Origin
#Algorithms #DataStructure #heap #leetcode #python3 #Hash_Table
Time: O(n log k)
Space: O(n)
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 1 and k == 1:
            return points

        distance = lambda x: (x[0] ** 2 + x[1] ** 2)
        min_heap = [(distance(x), x) for x in points]
        heapq.heapify(min_heap)

        result = []
        while k:
            k -= 1
            _, point = heapq.heappop(min_heap)
            result.append(point)

        return result
