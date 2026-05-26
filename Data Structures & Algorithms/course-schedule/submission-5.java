class Solution {
    // Time Complexity: O(V + E)
    // Space Complexity: O(V + E)
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses == 1) return true;
        if (prerequisites.length == 0) return true;

        int[] inDegree = new int[numCourses];
        List<Integer>[] adjList = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            adjList[i] = new ArrayList<>();
        }

        // build inDegre and adjList
        for (int[] pre : prerequisites) {
            inDegree[pre[0]]++;
            adjList[pre[1]].add(pre[0]);
        }

        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                q.add(i);
            }
        }
        int visitedCount = 0;
        while (!q.isEmpty()) {
            int course = q.poll();
            visitedCount++;
            for (int nextCourse : adjList[course]) {
                inDegree[nextCourse]--;
                if (inDegree[nextCourse] == 0) {
                    q.add(nextCourse);
                }
            }
        }

        return visitedCount == numCourses;
    }    
}
