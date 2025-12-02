def minPath(grid, k):
    def get_neighbors(row, col):
        return [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]

    def calculate_min_path(path, row, col, k, grid, visited, result):
        if k == 0:
            return result
        for neighbor in get_neighbors(row, col):
            n_row, n_col = neighbor
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]) and not visited[n_row][n_col]:
                visited[n_row][n_col] = True
                result.append(grid[n_row][n_col])
                if calculate_min_path(path + 1, n_row, n_col, k - 1, grid, visited, result):
                    return result
                result.pop()
                visited[n_row][n_col] = False
        return None

    result = None
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            visited = [[False] * len(grid[0]) for _ in range(len(grid))]
            visited[row][col] = True
            result = calculate_min_path(1, row, col, k, grid, visited, [grid[row][col]])
            if result:
                return result
    return []

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()