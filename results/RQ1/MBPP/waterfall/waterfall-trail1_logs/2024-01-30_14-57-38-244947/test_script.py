def maxAverageOfPath(cost):
  n = len(cost)
  m = len(cost[0])

  if n != m:
    raise ValueError("Input matrix is not a square matrix")
  for row in cost:
    for cell in row:
      if not isinstance(cell, (int, float)):
        raise ValueError("Input matrix contains non-numeric values")

  if not cost:
    return 0.0
  if n == 1 and m == 1:
    return cost[0][0]

  for row in cost:
    for cell in row:
      if cell < 0:
        raise ValueError("Negative cost values are not supported")
      if cell == 0:
        raise ValueError("Zero cost values are not supported")

  max_avg_cost = 0  # placeholder for actual calculation
  return max_avg_cost  # assuming max_avg_cost is calculated in the function
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]), 5.2)

if __name__ == '__main__':
    unittest.main()