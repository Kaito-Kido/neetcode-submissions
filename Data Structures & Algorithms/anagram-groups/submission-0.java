class Solution {
    // Time Complexity: O(m * n)
    // Space Complexity: O(n * m)
    public List<List<String>> groupAnagrams(String[] strs) {
        // Map này lưu key là tần suất và value là danh sách các từ
        Map<String, List<String>> map = new HashMap<>();
        
        for (String s : strs) {
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }

            // Dùng StringBuilder để xây dựng key hiệu quả
            StringBuilder sb = new StringBuilder();
            for (int i : count) {
                sb.append('#'); // Dùng # làm phân cách
                sb.append(i);
            }
            String key = sb.toString();

            // Dùng computeIfAbsent để code ngắn gọn và tránh lỗi List.of
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(map.values());
    }
}