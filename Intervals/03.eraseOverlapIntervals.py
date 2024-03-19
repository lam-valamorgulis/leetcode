# https://leetcode.com/problems/non-overlapping-intervals/


class Solution:

  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if not intervals:
      return 0

    intervals.sort(key=self.get_start_time)
    res = [intervals[0]]

    for interval in intervals[1:]:
      if interval[0] < res[-1][1]:  # If there is overlap
        res[-1][1] = min(res[-1][1], interval[1])  # Merge intervals
      else:
        res.append(interval)  # No overlap, add interval to result

    return len(intervals) - len(res)

  def get_start_time(self, interval: List[int]) -> int:
    return interval[0]
