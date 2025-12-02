def will_it_fly(q, w):
    left = 0
    right = len(q) - 1
    while left < right:
        if q[left] != q[right]:
            return False
        left += 1
        right -= 1
    return sum(q) <= w

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Balanced List with Maximum Weight",
      "Input Data": "q=[1,2,1], w=5",
      "Expected Output": "False"
    },
    {
      "Test Title": "Unbalanced List with Maximum Weight",
      "Input Data": "q=[3,2,3], w=1",
      "Expected Output": "False"
    },
    {
      "Test Title": "Balanced List with Maximum Weight",
      "Input Data": "q=[3,2,3], w=9",
      "Expected Output": "True"
    },
    {
      "Test Title": "Single Element List with Maximum Weight",
      "Input Data": "q=[3], w=5",
      "Expected Output": "True"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(will_it_fly([1, 2], 5), False)

    def test2(self):
        self.assertEqual(will_it_fly([3, 2, 3], 1), False)

    def test3(self):
        self.assertEqual(will_it_fly([3, 2, 3], 9), True)

    def test4(self):
        self.assertEqual(will_it_fly([3], 5), True)

if __name__ == '__main__':
    unittest.main()