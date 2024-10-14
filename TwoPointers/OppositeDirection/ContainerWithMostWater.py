# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
from typing import List


def container_with_most_water(heights: List[int]) -> int:
  l, r = 0, len(heights) - 1
  max_area = 0
  while l < r:
    area = (r - l) * min(heights[l], heights[r])
    max_area = max(area, max_area)
    if heights[l] < heights[r]:
      l += 1
    else:
      r -= 1
  return max_area
