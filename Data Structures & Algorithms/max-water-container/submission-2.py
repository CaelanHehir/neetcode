class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nb_bars = len(heights)
        max_water = 0

        left = 0
        right = nb_bars - 1
        while left < right:
            water_level = min(heights[left], heights[right]) * (right - left)
            max_water = max(max_water, water_level)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water
