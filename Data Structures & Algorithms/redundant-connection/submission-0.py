class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        
        def find(v):
            if parent[v] == v:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(u, v):
            rootU = find(u)
            rootV = find(v)
            
            if rootU == rootV:
                return False
            
            if rank[rootU] > rank[rootV]:
                parent[rootV] = rootU
            elif rank[rootV] > rank[rootU]:
                parent[rootU] = rootV
            else:
                parent[rootV] = rootU
                rank[rootU] += 1
            return True
                
        for u, v in edges:
            notConnect = union(u, v)
            if not notConnect:
                return [u, v]
        return []