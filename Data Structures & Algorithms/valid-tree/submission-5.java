class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (n - 1 != edges.length)
            return false;

        List<Integer>[] adjList = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adjList[i] = new ArrayList<>();
        }

        for (int[] e : edges) {
            adjList[e[0]].add(e[1]);
            adjList[e[1]].add(e[0]);
        }
        boolean[] visited = new boolean[n];
        if (haveCycle(0, -1, adjList, visited))
            return false;

        int count = 0;
        for (int i = 0; i < visited.length; i++) {
            if (visited[i]) count++;
        }

        return n == count;
    }

    public boolean haveCycle(int node, int parent, List<Integer>[] adjList, boolean[] visited) {
        visited[node] = true;
        for (int neighbor : adjList[node]) {
            if (neighbor == parent)
                continue;

            if (visited[neighbor] == true)
                return true;

            if (haveCycle(neighbor, node, adjList, visited))
                return true;
        }

        return false;
    }
}
