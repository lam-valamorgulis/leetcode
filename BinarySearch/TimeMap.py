# https://leetcode.com/problems/time-based-key-value-store/
# Key solution :
# know to to initize the data structure optimize for search :
# - hash map table (1 key, 1 value)
# binary search must be in sorting ascending or descending order
#  the value is in ascending order by time stamp
#  compared value l , r


class TimeMap(object):

  def __init__(self):
    # init data structure:
    self.data = {}
    # key: list of [value, timestamp]
    # the value ascending by timestamp

  def set(self, key, value, timestamp):
    if key not in self.data:
      self.data[key] = []

    self.data[key].append([value, timestamp])

  # get the key then access to the list of value of
  # that is which is a list of [value, timestamp] ascending by time
  def get(self, key, timestamp):

    # since the timestamps are always given in incresing order that means our list is already sorted (hooray!)
    # since its sorted we can do something faster than O(n) aka O(logn) w/ binary search
    values = self.data.get(key, [])
    l, r = 0, len(values) - 1
    res = ""
    while l <= r:
      m = (l + r) // 2

      if values[m][1] <= timestamp:
        res = values[m][0]
        l = m + 1
      else:
        r = m - 1

    return res


timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
timeMap.set("foo", "bar2", 3)
val = timeMap.get("foo", 4)

print(val)
