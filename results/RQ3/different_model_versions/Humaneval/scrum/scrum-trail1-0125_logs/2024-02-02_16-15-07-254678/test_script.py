def car_race_collision(n: int):
    collisions = n*(n-1)//2
    return collisions

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "All cars collide at the same time",
      "Input Data": "n=5",
      "Expected Output": "10"
    },
    {
      "Test Title": "No collisions",
      "Input Data": "n=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Different numbers of cars moving in different directions",
      "Input Data": "n_left=3, n_right=2",
      "Expected Output": "6"
    },
    {
      "Test Title": "Edge case: large number of cars",
      "Input Data": "n=100",
      "Expected Output": "4950"
    },
    {
      "Test Title": "Cars colliding at different times",
      "Input Data": "n=3",
      "Expected Output": "3"
    },
    {
      "Test Title": "Cars colliding at the same time but with different speeds",
      "Input Data": "n_left=2, n_right=2",
      "Expected Output": "2"
    },
    {
      "Test Title": "Boundary value analysis: minimum number of cars",
      "Input Data": "n=1",
      "Expected Output": "0"
    },
    {
      "Test Title": "Boundary value analysis: maximum number of cars",
      "Input Data": "n=1000",
      "Expected Output": "499500"
    },
    {
      "Test Title": "Equivalence partitioning test: different ranges of input data",
      "Input Data": "n=500",
      "Expected Output": "124750"
    }
  ]
}
import unittest


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(car_race_collision(1), 0)
        self.assertEqual(car_race_collision(2), 1)
        self.assertEqual(car_race_collision(3), 3)
        self.assertEqual(car_race_collision(4), 6)
        self.assertEqual(car_race_collision(5), 10)

if __name__ == '__main__':
    unittest.main()