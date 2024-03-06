# https://leetcode.com/problems/k-closest-points-to-origin/description/

import heapq
import math


class Solution:

  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    distances = {}
    for point in points:
      distance = math.sqrt(point[0]**2 + point[1]**2)
      if distance in distances:
        distances[distance].append(point)
      else:
        distances[distance] = [point]

    closest_points = []
    for distance in sorted(distances.keys()):
      for point in distances[distance]:
        closest_points.append(point)
        if len(closest_points) == k:
          return closest_points
