class Solution {
    // Time Complexity: O(V + E)
    // Space Complexity: O(V + E)
    public int countComponents(int n, int[][] edges) {
        if (n == 1)
            return 1;
        List<Integer>[] adjList = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adjList[i] = new ArrayList<>();
        }

        for (int[] e : edges) {
            adjList[e[0]].add(e[1]);
            adjList[e[1]].add(e[0]);
        }

        int count = 0;
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                count++;
                Queue<Integer> q = new ArrayDeque<>();
                visited[i] = true;
                q.add(i);

                while (!q.isEmpty()) {
                    int currentNode = q.poll();
                    List<Integer> adjs = adjList[currentNode];

                    for (Integer adj : adjs) {
                        if (visited[adj] == false) {
                            visited[adj] = true;
                            q.add(adj);
                        }
                    }
                }
            }
        }

        return count;
    }
}
