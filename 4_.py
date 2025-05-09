from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = sorted(nums1 + nums2)
        temp = len(new_nums)//2 
        if len(new_nums)%2 == 1:
            return new_nums[temp]
        else:
            return (new_nums[temp-1] + new_nums[temp])/2
print(Solution().findMedianSortedArrays([1,3],[2,4]))