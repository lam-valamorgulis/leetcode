# how to get value with O(1) time => using hashmap table
# put function how to know the least recently used ?
# put to the node have been interated to the end
# delete the node when capacity is full
# => move,add node => using double linked list
# hashmap to fast lookup, double linked to control recent used : by move node to end,
# or add node to end


class LRUCache(object):

  class Node:

    def __init__(self, key, value):
      self.key = key
      self.value = value
      self.prev = None
      self.next = None

  def __init__(self, capacity):
    self.capacity = capacity
    self.cache = {}  # hash map for fast looking a node
    self.head = self.Node(0, 0)
    self.tail = self.Node(0, 0)
    # double linked list :
    self.head.next = self.tail
    self.tail.prev = self.head

  # internal helper function
  def _move_to_end(self, node):
    # Move a node to the end of the linked list (most recently used)
    node.prev.next = node.next
    node.next.prev = node.prev
    self._add_to_end(node)

  def _add_to_end(self, node):
    # Add a node to the end of the linked list
    prev_tail = self.tail.prev
    prev_tail.next = node
    node.prev = prev_tail
    node.next = self.tail
    self.tail.prev = node

  def get(self, key):
    if key in self.cache:
      # If key exists, move the node to the end (recently used) and return its value
      node = self.cache[key]
      self._move_to_end(node)
      return node.value
    return -1

  def put(self, key, value):
    if key in self.cache:
      # If key exists, update its value and move the node to the end
      node = self.cache[key]
      node.value = value
      self._move_to_end(node)
    else:
      # If key doesn't exist, add a new node to the end
      if len(self.cache) >= self.capacity:
        # If capacity is reached, evict the least recently used node (head.next)
        del_key = self.head.next.key
        del self.cache[del_key]
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
      new_node = self.Node(key, value)
      self.cache[key] = new_node
      self._add_to_end(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
