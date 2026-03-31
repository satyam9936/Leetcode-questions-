# Leetcode 2316
from ast import List


class CountUnreachablePairs:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = []

        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for i in range(n):
            if i not in visited:
                component = []
                dfs(i, component)
                components.append(component)

        total_pairs = 0
        for component in components:
            size = len(component)
            total_pairs += size * (n - size)

        return total_pairs // 2