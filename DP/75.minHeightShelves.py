# https://leetcode.com/problems/filling-bookcase-shelves/


class Solution:

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @lru_cache(None)
        def minHeight(i):
            if i == n:
                return 0

            width = 0
            height = 0
            minHeightResult = float('inf')

            for j in range(i, n):
                width += books[j][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j][1])
                minHeightResult = min(minHeightResult,
                                      height + minHeight(j + 1))

            return minHeightResult

        return minHeight(0)
