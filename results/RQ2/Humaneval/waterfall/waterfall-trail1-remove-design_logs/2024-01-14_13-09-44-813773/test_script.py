def add(x: int, y: int) -> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Inputs must be integers")
    
    return x + y

assert add(0, 0) == 0
assert add(-1, 1) == 0
assert add(1000000, 2000000) == 3000000

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Addition of positive numbers",
      "Input Data": "x=1, y=2",
      "Expected Output": "3"
    },
    {
      "Test Title": "Addition of negative numbers",
      "Input Data": "x=-1, y=-2",
      "Expected Output": "-3"
    },
    {
      "Test Title": "Addition of positive and negative numbers",
      "Input Data": "x=-1, y=2",
      "Expected Output": "1"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()