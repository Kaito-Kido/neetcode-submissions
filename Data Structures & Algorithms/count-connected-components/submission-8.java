class Solution {
    // Time Complexity: O(V + E)
    // Space Complexity: O(V + E)
    public int countComponents(int n, int[][] edges) {
        DSU dsu = new DSU(n);
        for (int[] e : edges) {
            dsu.union(e[0], e[1]);
        }

        return dsu.getCounts();
    }

    public static class DSU {
        private int[] parent;
        private int[] rank;
        private int count;

        DSU(int n) {
            this.count = n;
            this.parent = new int[n];
            this.rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
        }

        public int find(int v) {
            if (parent[v] == v) {
                return v;
            }

            return parent[v] = find(parent[v]);
        }

        public void union(int i, int j) {
            int rootI = find(i);
            int rootJ = find(j);

            if (rootI == rootJ) return;

            if (rank[rootI] > rank[rootJ]) {
                parent[rootJ] = rootI;
            } else if (rank[rootI] < rank[rootJ]) {
                parent[rootI] = rootJ;
            } else {
                parent[rootJ] = rootI;
                rank[rootI]++;
            }
            count--;
        }

        public int getCounts() {
            return this.count;
        }
    }
}
