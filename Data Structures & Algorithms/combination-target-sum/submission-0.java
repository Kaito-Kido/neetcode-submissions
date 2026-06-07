

class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        // 1. Sắp xếp để đảm bảo thứ tự tăng dần
        Arrays.sort(nums);
        backtrack(nums, target, result, new ArrayList<>(), 0);
        return result;
    }

    private void backtrack(int[] nums, int target, List<List<Integer>> result, List<Integer> current, int start) {
        if (target == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i < nums.length; i++) {
            // Nếu số hiện tại đã lớn hơn target thì không cần xét các số sau nữa (vì đã sort)
            if (nums[i] > target) break;

            current.add(nums[i]);
            
            // 2. Truyền 'i' vào để được phép dùng lại chính nó
            // 3. Không bao giờ truyền giá trị nhỏ hơn 'i', nên không bao giờ tạo ra được hoán vị [5, 2, 2]
            backtrack(nums, target - nums[i], result, current, i);
            
            // Backtrack
            current.remove(current.size() - 1);
        }
    }
}