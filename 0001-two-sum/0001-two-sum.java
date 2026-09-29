class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hasher = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (hasher.containsKey(complement)) {
                return new int[] { hasher.get(complement), i };
            }

            hasher.put(nums[i], i);
        }

        return new int[] {};
    }
}