class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses == 1) return true;
        if (prerequisites.length == 0) return true;

        // Thay HashMap bằng Array of Lists để tối ưu RAM và tốc độ truy cập O(1)
        List<Integer>[] adjList = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            adjList[i] = new ArrayList<>();
        }

        // Xây dựng đồ thị
        for (int[] pre : prerequisites) {
            int course = pre[0];
            int prerequisite = pre[1];
            adjList[prerequisite].add(course);
        }

        // 0 = haven't visited
        // 1 = current on the way
        // 2 = safe
        int[] coloring = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (coloring[i] == 0) {
                if(!dfs(i, coloring, adjList)) return false;
            }
        }
        return true;
    }

    public boolean dfs(int course ,int[] coloring, List<Integer>[] adjList) {
        if (coloring[course] == 1) return false;
        if (coloring[course] == 2) return true;
        coloring[course] = 1;
        List<Integer> nextCourses = adjList[course];
        for (Integer nextCourse : nextCourses) {
            boolean result = dfs(nextCourse, coloring, adjList);
            if (!result) return result;
        } 
        coloring[course] = 2;
        return true;
    }
}
