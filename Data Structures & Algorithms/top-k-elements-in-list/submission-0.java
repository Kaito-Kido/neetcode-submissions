class Solution {
    // Time Complexity: O(n + mlogk) với m là số lượng sau khi tính frequency
    // Space Complextity: O(m)
    // m <= n
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        Queue<Map.Entry<Integer, Integer>> heap =
            new PriorityQueue<>((a, b) -> a.getValue() - b.getValue());

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            heap.offer(entry);

            if (heap.size() > k) {
                heap.poll();
            }
        }

        int[] result = new int[heap.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = heap.poll().getKey();
        }

        return result;
    }
}
