class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        targets = []
        i = 0
        for i in range(len(nums)):
            if nums[i] == val:
                targets.append(nums[i])

        for value in targets:
            nums.remove(value)

        return len(nums)