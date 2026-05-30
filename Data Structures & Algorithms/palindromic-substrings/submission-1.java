class Solution {
    public int countSubstrings(String s) {
        if (s == null || s.length() == 0) return 0;
        int totalCount = 0;

        for (int i = 0; i < s.length(); i++) {
            // Trường hợp 1: Tâm là 1 ký tự (độ dài lẻ, ví dụ: "aba")
            totalCount += expandAndCount(s, i, i);
            
            // Trường hợp 2: Tâm là khoảng giữa 2 ký tự (độ dài chẵn, ví dụ: "abba")
            totalCount += expandAndCount(s, i, i + 1);
        }

        return totalCount;
    }

    private int expandAndCount(String s, int left, int right) {
        int count = 0;
        // Mở rộng ra 2 phía miễn là ký tự ở left và right bằng nhau
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            count++; // Cứ mỗi bước thỏa mãn là tìm thêm được 1 chuỗi đối xứng
            left--;
            right++;
        }
        return count;
    }
}