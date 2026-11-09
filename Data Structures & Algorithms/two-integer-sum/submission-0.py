class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans_set = {}

        for i, n in enumerate(nums):
            ans_set[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in ans_set and ans_set[diff] != i:
                return [i, ans_set[diff]]
        
        return []
        