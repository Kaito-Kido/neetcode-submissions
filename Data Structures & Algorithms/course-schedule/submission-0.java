class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses == 1) return true;
        if (prerequisites.length == 0) return true;
        Map<Integer, List<Integer>> adjMap = new HashMap<>((int)(numCourses / 0.75) + 1);

        for (int[] pre : prerequisites) {
            if (!adjMap.containsKey(pre[1])) {
                adjMap.put(pre[1], new ArrayList<>());
            }

            adjMap.get(pre[1]).add(pre[0]);
        }

        // 0 = haven't visited
        // 1 = current on the way
        // 2 = safe
        int[] coloring = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if(!dfs(i, coloring, adjMap)) return false;
        }
        return true;
    }

    public boolean dfs(int course ,int[] coloring, Map<Integer, List<Integer>> adjMap) {
        if (coloring[course] == 1) return false;
        if (coloring[course] == 2) return true;
        coloring[course] = 1;
        List<Integer> nextCourses = adjMap.getOrDefault(course, new ArrayList<>());
        for (Integer nextCourse : nextCourses) {
            boolean result = dfs(nextCourse, coloring, adjMap);
            if (!result) return result;
        } 
        coloring[course] = 2;
        return true;
    }
}
