from random import choice

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)

        while True:
            target = choice(nums)
            if nums.count(target) > length // 2:
                return target
