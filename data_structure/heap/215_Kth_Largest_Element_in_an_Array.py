class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k <= 0 or k > len(nums):
            return None

        min_heap = [i for i in nums[:k]]
        heapq.heapify(min_heap)

        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])

        return min_heap[0]
