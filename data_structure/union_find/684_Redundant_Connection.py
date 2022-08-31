from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # The number of `edge` should be the number of `node` - 1
        # Here define number of `edge` as n,
        # since there is a redundant connection
        parent = [i for i in range(n + 1)]

        def find(idx: int) -> int:
            if parent[idx] != idx:
                parent[idx] = find(parent[idx])
            return parent[idx]

        def union(idx1: int, idx2: int) -> None:
            parent[find(idx1)] = find(idx2)

        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                # Here is the Redundant Connection
                return [node1, node2]

        return None
