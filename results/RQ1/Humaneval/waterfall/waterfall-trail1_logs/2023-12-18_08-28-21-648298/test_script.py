def prod_signs(arr):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        return "Input must be a list of integers"
    
    if len(arr) == 0:
        return None
    
    product_of_signs = 1
    sum_of_magnitudes = 0
    for num in arr:
        product_of_signs *= 1 if num > 0 else -1 if num < 0 else 0
        sum_of_magnitudes += abs(num)
    
    return product_of_signs * sum_of_magnitudes

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Input Array Test",
      "Input Data": "[]",
      "Expected Output": "None"
    },
    {
      "Test Title": "Positive and Negative Integers Test",
      "Input Data": "[1, 2, 2, -4]",
      "Expected Output": "-9"
    },
    {
      "Test Title": "Input Array with Zero Values Test",
      "Input Data": "[0, 1]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Large Input Array Test",
      "Input Data": "[100, 200, -200, 400, -500, 600]",
      "Expected Output": "None"
    },
    {
      "Test Title": "Non-Integer Inputs Test",
      "Input Data": "['abc', 'def']",
      "Expected Output": "None"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_prod_signs(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([]), None)

if __name__ == '__main__':
    unittest.main()