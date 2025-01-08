from typing import List


# 第一次提交
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         target_dict = {}
#         for i, item in enumerate(nums):
#             if target-item in target_dict:
#                 return target_dict[target-item], i
#             else:
#                 target_dict[item] = i


# 第二次提交
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums = sorted((num,i) for i,num in enumerate(nums))
        
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left][0] + nums[right][0] == target:
                return nums[left][1], nums[right][1]
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                right -= 1

print(Solution().twoSum([3,2,4], 6))