class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();

        for (String s : strs) {
            encoded.append(s.length() + "_" + s);
        }
        return encoded.toString();
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int startIndex = 0;
        while (startIndex < str.length()) {
            int endIndex = startIndex + 1;
            while (endIndex < str.length() && str.charAt(endIndex) != '_') {
                endIndex++;
            }
            Integer nextDigit = Integer.valueOf(str.substring(startIndex, endIndex));

            result.add(str.substring(endIndex + 1, endIndex + 1 + nextDigit));
            startIndex = endIndex + 1 + nextDigit;
        }

        return result;
    }
}
