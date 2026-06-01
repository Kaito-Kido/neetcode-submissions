class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        Map<Integer, Integer> map  = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], 1);
        }

        int max = 1;
        Set<Integer> visited = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (visited.contains(nums[i])) continue;

            int head = nums[i];
            while (map.containsKey(head - 1)) {
                head = head - 1;
            }

            visited.add(head);
            while (map.containsKey(head + 1)) {
                map.put(head + 1, map.get(head + 1) + map.get(head));
                max = Math.max(max, map.get(head + 1));
                head = head + 1;
                visited.add(head);
            }
        }

        return max;
    }
}
