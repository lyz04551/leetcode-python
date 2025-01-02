from typing import List


# 第一次提交
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        for i, item in enumerate(nums):
            if target-item in target_dict:
                return target_dict[target-item], i
            else:
                target_dict[item] = i

