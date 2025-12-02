import math
class Graph:
    def __init__(self, grid):
        self.grid = grid

    def get_neighbors(self, node):
        neighbors = []
        rows, cols = len(self.grid), len(self.grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            r, c = node[0] + dr, node[1] + dc
            if 0 <= r < rows and 0 <= c < cols and self.grid[r][c] == 1:
                neighbors.append((r, c))
        return neighbors

class BFS:
    def __init__(self, graph, grid):
        self.graph = graph
        self.grid = grid

    def bfs(self, start):
        visited = set()
        queue = [start]
        buckets_lowered = 0

        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            r, c = node
            if self.grid[r][c] == 1:
                buckets_lowered += 1
                self.grid[r][c] = 0
            for neighbor in self.graph.get_neighbors(node):
                queue.append(neighbor)
        return buckets_lowered

def max_fill(grid, capacity):
    graph = Graph(grid)
    bfs = BFS(graph, grid)

    total_buckets_lowered = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                total_buckets_lowered += bfs.bfs((r, c))
    return total_buckets_lowered // capacity
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1), 6)
    
    def test_example2(self):
        self.assertEqual(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2), 5)

    def test_example3(self):
        self.assertEqual(max_fill([[0,0,0], [0,0,0]], 5), 0)

if __name__ == '__main__':
    unittest.main()