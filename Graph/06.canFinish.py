# https://leetcode.com/problems/course-schedule/

# Building Adjacency List: The code initializes a dictionary graph to store the adjacency list for each course. It iterates over the range of numCourses and initializes an empty list for each course. Then, it populates the adjacency list with prerequisites.
# DFS and Cycle Detection: It defines a DFS function dfs(course) to check if it's possible to finish the course. It recursively explores prerequisites for each course. It uses a visited set to track courses visited during DFS traversal, avoiding revisiting courses and detecting cycles.
# DFS Function: The DFS function dfs(course) checks if the course is already visited. If so, it returns False to indicate a cycle. If there are no prerequisites for the course, it returns True. Otherwise, it recursively calls dfs(pre) for each prerequisite. It removes the course from the visited set after DFS is completed.
# Main Logic: The code iterates through each course and runs DFS. If DFS returns False for any course, indicating a cycle, it returns False. If DFS completes for all courses without any cycles, it returns True.

# This code uses DFS to check if it's possible to complete all courses without any cycle in prerequisites. If any cycle is found, it returns False; otherwise, it returns True.


class Solution(object):

  def canFinish(self, numCourses, prerequisites):
    # create hashmap for adjanct course of each course
    # run a dfs on each of course to check whether or not each adjancy course can be finished ?
    # 1. create adjancy list:
    graph = {}

    for course in range(numCourses):
      graph[course] = []
    for course, prerequisite in prerequisites:
      graph[course].append(prerequisite)

    # 2. tracking a visited course:
    visited = set()

    # 3. make a dfs of each course
    def dfs(crs):
      if crs in visited:
        return False
      if graph[crs] == []:
        return True
      # mark crs as visited
      visited.add(crs)
      for pre in graph[crs]:
        if not dfs(pre):
          return False
      visited.remove(crs)
      graph[crs] = []
      return True

    # 4. run a dfs on each course:
    for crs in range(numCourses):
      if not dfs(crs):
        return False

    return True
