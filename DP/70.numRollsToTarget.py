# https://leetcode.com/problems/video-stitching/

 class Solution:
     def videoStitching(self, clips: List[List[int]], time: int) -> int:
             # Initialize dp array with infinity and dp[0] with 0
         dp = [float('inf')] * (time + 1)
         dp[0] = 0

         # Iterate over each time point
         for t in range(1, time + 1):
             # Iterate over all clips
             for start, end in clips:
                 if start <= t <= end:
                     dp[t] = min(dp[t], dp[start] + 1)

         # If dp[time] is still infinity, return -1
         return -1 if dp[time] == float('inf') else dp[time]


