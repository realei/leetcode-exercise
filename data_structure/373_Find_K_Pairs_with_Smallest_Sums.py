class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        min_heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        # not necessary to do heapify, since both array nums1 and nums 2 are sorted with ascending
        # heapq.heapify(min_heap)
        while min_heap and len(ans) < k:
            _, i, j = heapq.heappop(min_heap)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans
