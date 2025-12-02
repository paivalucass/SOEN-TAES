def is_equal_to_sum_even(n):
    if not isinstance(n, int) or n < 0:
        return False
    
    count = 0
    for i in range(2, n // 2 + 1, 2):
        for j in range(i, n // 2 + 1, 2):
            for k in range(j, n // 2 + 1, 2):
                for l in range(k, n // 2 + 1, 2):
                    if i + j + k + l == n:
                        count += 1
    
    return count > 0

# Test Cases:
{
  "requirement analysis": "evaluation",
  "test_cases": [
    {
      "Test Title": "Positive Even Numbers Sum Test",
      "Input Data": "parameter1=4",
      "Expected Output": "False"
    },
    {
      "Test Title": "Positive Even Numbers Sum Test",
      "Input Data": "parameter1=6",
      "Expected Output": "False"
    },
    {
      "Test Title": "Positive Even Numbers Sum Test",
      "Input Data": "parameter1=8",
      "Expected Output": "True"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_equal_to_sum_even(4), False)
        self.assertEqual(is_equal_to_sum_even(6), False)
        self.assertEqual(is_equal_to_sum_even(8), True)

if __name__ == '__main__':
    unittest.main()