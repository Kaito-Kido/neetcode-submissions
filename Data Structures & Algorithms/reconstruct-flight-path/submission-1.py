# Requirement
# - Use all tickets
# - At least one valid path use all of tickets
# Invariant
# 

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        stack = []
        adjList = defaultdict(list)

        # O(V)
        for source, dest in tickets:
            adjList[source].append(dest)

        
        # O(V*(E-1)log(E-1))
        for source in adjList.keys():
            adjList[source].sort(reverse=True)

        def dfs(source):
            if len(adjList[source]) == 0:
                stack.append(source)
                return
            
            while (len(adjList[source]) > 0):
                dest = adjList[source].pop()
                dfs(dest)
            stack.append(source)
            return
        dfs("JFK")
        return stack[::-1]



