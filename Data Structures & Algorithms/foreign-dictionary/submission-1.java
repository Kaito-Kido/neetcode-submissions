class Solution {
    public String foreignDictionary(String[] words) {
        Map<Character, Set<Character>> adj = new HashMap<>();
        Map<Character, Integer> inDegree = new HashMap<>();

        // 1. Khởi tạo tất cả các ký tự có trong words vào Map
        for (String w : words) {
            for (char c : w.toCharArray()) {
                adj.putIfAbsent(c, new HashSet<>());
                inDegree.putIfAbsent(c, 0);
            }
        }

        // 2. Build đồ thị
        for (int i = 0; i < words.length - 1; i++) {
            String first = words[i];
            String second = words[i + 1];
            
            // Kiểm tra trường hợp đặc biệt: "abc", "ab" -> không hợp lệ
            if (first.length() > second.length() && first.startsWith(second)) return "";

            for (int j = 0; j < Math.min(first.length(), second.length()); j++) {
                char c1 = first.charAt(j);
                char c2 = second.charAt(j);
                if (c1 != c2) {
                    // Dùng Set để tránh trùng cạnh (câu hỏi của bạn)
                    if (!adj.get(c1).contains(c2)) {
                        adj.get(c1).add(c2);
                        inDegree.put(c2, inDegree.get(c2) + 1);
                    }
                    break; // Chỉ xét ký tự khác biệt đầu tiên
                }
            }
        }

        // 3. BFS (Kahn's Algorithm)
        Queue<Character> queue = new LinkedList<>();
        for (char c : inDegree.keySet()) {
            if (inDegree.get(c) == 0) queue.add(c);
        }

        StringBuilder sb = new StringBuilder();
        while (!queue.isEmpty()) {
            char curr = queue.poll();
            sb.append(curr);

            for (char neighbor : adj.get(curr)) {
                inDegree.put(neighbor, inDegree.get(neighbor) - 1);
                if (inDegree.get(neighbor) == 0) {
                    queue.add(neighbor);
                }
            }
        }

        // 4. Nếu độ dài chuỗi tạo ra không bằng số lượng ký tự duy nhất -> có chu trình
        return sb.length() == inDegree.size() ? sb.toString() : "";
    }
}