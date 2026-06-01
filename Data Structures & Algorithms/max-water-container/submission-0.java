class Solution {
    public int maxArea(int[] height) {
        int startIndex = 0;
        int endIndex = height.length - 1;
        int water = 0;
        while (startIndex < endIndex) {
            water = Math.max(water, (endIndex - startIndex) * Math.min(height[startIndex], height[endIndex]));
            if (height[startIndex] <= height[endIndex]) {
                startIndex++;
            } else {
                endIndex--;
            }
        }

        return water;
    }
}