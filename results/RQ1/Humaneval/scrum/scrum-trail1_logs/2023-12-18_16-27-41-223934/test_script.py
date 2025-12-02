def is_equal_to_sum_even(n):
    """
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    count = 0
    for i in range(2, n//2 + 1):
        for j in range(i, n//2 + 1):
            for k in range(j, n//2 + 1):
                l = n - i - j - k
                if l % 2 == 0 and l >= k:
                    count += 1
                    if count > 1:
                        return False
    if count == 1:
        return True
    else:
        return False

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Negative Even Number",
      "Input Data": "parameter1=-4",
      "Expected Output": "False"
    },
    {
      "Test Title": "Zero",
      "Input Data": "parameter1=0",
      "Expected Output": "False"
    },
    {
      "Test Title": "Large Even Number",
      "Input Data": "parameter1=100",
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