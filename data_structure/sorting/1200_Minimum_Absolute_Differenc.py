from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()

        min_diff, ans = float('inf'), []
        for i in range(n - 1):
            delta = arr[i + 1] - arr[i]
            if delta < min_diff:
                min_diff = delta
                ans = [[arr[i], arr[i+1]]]
            elif delta == min_diff:
                ans.append([arr[i], arr[i+1]])

        return ans
