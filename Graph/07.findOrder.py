# https://leetcode.com/problems/course-schedule-ii/


class Solution(object):

  def findOrder(self, numCourses, prerequisites):
    # 1.make a graph of adjancy list:
    graph = {}
    for num in range(numCourses):
      graph[num] = []

    for crs, pre in prerequisites:
      graph[crs].append(pre)

    # creat list output
    output = []

    # 2. create 2 set visit (remember crs visit) and cycle (check cycle)
    visit = set()
    cycle = set()

    # 2.make a dfs
    def dfs(crs):
      if crs in cycle:
        return False
      if crs in visit:
        return True

      # tracking if meet crs in the cycle
      cycle.add(crs)
      for pre in graph[crs]:
        if dfs(pre) == False:
          return False

      # remove crs of cycle
      cycle.remove(crs)
      # add crs to visit
      visit.add(crs)
      # add to the output
      output.append(crs)
      return True

    for n in range(numCourses):
      if dfs(n) == False:
        return []
    return output
