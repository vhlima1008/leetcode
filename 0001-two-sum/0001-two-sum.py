class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for idx, i in enumerate(nums):
            if hasher.get(i) is not None:
                return[hasher.get(i), idx]
            hasher[target - i] = idx