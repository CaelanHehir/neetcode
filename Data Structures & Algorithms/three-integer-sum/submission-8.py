class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        triplets = []
        for i in range(length):
            j = i + 1
            k = length - 1
            while j < k:
                if j == i:
                    j += 1
                    continue
                if k == i:
                    k -= 1
                    continue
                if nums[j] + nums[k] < -nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in triplets:
                        triplets.append(triplet)
                    j += 1
                    k -= 1
        return triplets
