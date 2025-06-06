from typing import List
from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Sorted list of all obstacles (initially with a virtual obstacle at position 0)
        axis = SortedList()
        max_x = max(q[1] for q in queries)  # Maximum x value to size the segment tree
        gaps = SegTree(max_x)  # Segment tree to store max gap between consecutive obstacles
        
        axis.add(0)        # Virtual start obstacle at position 0
        gaps.update(0, 0)  # Gap at position 0 is zero
        res = []

        for q in queries:
            if q[0] == 1:
                # Query type 1: Place an obstacle at position q[1]
                x = q[1]
                idx = axis.bisect(x)  # Position where x should be inserted

                # Update the interval to the next obstacle if it exists
                if idx < len(axis):
                    nxt = axis[idx]
                    gaps.update(nxt, nxt - x)

                # Update the interval from the previous obstacle to x
                prev = axis[idx - 1]
                gaps.update(x, x - prev)

                axis.add(x)  # Add the new obstacle
            else:
                # Query type 2: Can we place a block of size sz in range [0, x]?
                x, sz = q[1], q[2]
                idx = axis.bisect(x)
                prev = axis[idx - 1]  # Last obstacle before or at x

                # Max gap is either the gap from prev to x or the max known gap before prev
                max_gap = max(x - prev, gaps.query(prev))

                # If block size ≤ max_gap, it can be placed
                res.append(sz <= max_gap)

        return res

class SegTree:
    def __init__(self, n: int):
        # Round up to the next power of 2 for full binary tree representation
        self.n = 1 << (n.bit_length())
        self.tree = [0] * (2 * self.n)

    def update(self, ind: int, val: int):
        # Set value at leaf node and update its parents
        ind += self.n
        self.tree[ind] = val
        while ind > 1:
            ind //= 2
            self.tree[ind] = max(self.tree[ind * 2], self.tree[ind * 2 + 1])

    def query(self, ind: int) -> int:
        # Get max in range [0, ind]
        ind += self.n
        res = self.tree[ind]
        while ind > 1:
            if ind % 2 == 1:
                res = max(res, self.tree[ind - 1])
            ind //= 2
        return res
