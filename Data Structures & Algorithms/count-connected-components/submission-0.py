class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        visit = set()
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node):
            for nei in adj_list[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
        ans = 0
        for node in range(n):
            if node not in visit:
                ans += 1
                visit.add(node)
                dfs(node)

        return ans

        