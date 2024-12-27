from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        while k>0:
            nums.sort()
            nums[0]+=1
            k-=1
            print(nums)


        MOD = 10 ** 9 + 7
        product = 1
        for num in nums:
            product = product * num % MOD
        return product
    
print(Solution().maximumProduct([0,4],5))