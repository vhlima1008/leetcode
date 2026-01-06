class Solution:
    def twoSum(self, nums, target: int):
        hasher = {}
        for idx, i in enumerate(nums):
            if hasher.get(i) is not None:
                return[hasher.get(i), idx]
            hasher[target - i] = idx