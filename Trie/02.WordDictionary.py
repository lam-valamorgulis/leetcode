# https://leetcode.com/problems/design-add-and-search-words-data-structure/


class TrieNode():
  def __init__(self):
      self.child = {}
      self.end = False

class WordDictionary:
  def __init__(self):
      self.root = TrieNode()

  def addWord(self, word: str) -> None:
      curr = self.root
      for w in word:
          if w not in curr.child:
              curr.child[w] = TrieNode()
          curr = curr.child[w]
      curr.end = True

  def search(self, word: str) -> bool:
      def dfs(i,node):
          if i == len(word):
              return node.end

          c = word[i]
          if c == ".":
              for child in node.child.values():
                  if dfs(i+1,child):
                      return True
          else:
              if c in node.child:
                  return dfs(i+1,node.child[c])
          return False

      return dfs(0,self.root)


