def max_sub_array_sum(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far
{
  "test_cases": [
    {
      "Test Title": "Empty input list",
      "Input Data": "a=[], size=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "List with all negative integers",
      "Input Data": "a=[-1,-2,-3,-4]",
      "Expected Output": "-1"
    },
    {
      "Test Title": "List with all positive integers",
      "Input Data": "a=[1,2,3,4]",
      "Expected Output": "10"
    },
    {
      "Test Title": "List with mix of positive and negative integers",
      "Input Data": "a=[-2, -3, 4, -1, -2, 1, 5, -3]",
      "Expected Output": "7"
    },
    {
      "Test Title": "List with duplicate numbers",
      "Input Data": "a=[-2, -3, 4, -1, -2, 1, 5, -3, 4, -1]",
      "Expected Output": "9"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8), 7)

if __name__ == '__main__':
    unittest.main()