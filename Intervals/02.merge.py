# https://leetcode.com/problems/merge-intervals/


class Solution:

  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
      return []

    # Sort intervals based on the start time
    intervals.sort(key=self.get_start_time)

    res = [intervals[0]]

    for interval in intervals[1:]:
      if interval[0] <= res[-1][1]:  # If there is overlap
        res[-1][1] = max(res[-1][1], interval[1])  # Merge intervals
      else:
        res.append(interval)  # No overlap, add interval to result

    return res

  def get_start_time(self, interval: List[int]) -> int:
    return interval[0]
