def is_product_even(arr):
    if not arr:
        return False  # If the input list is empty, the product is not even
    product = 1
    for num in arr:
        if num % 2 != 0:
            return False  # If any number in the list is odd, the product is not even
        product *= num
    return product % 2 == 0  # Check if the product is even or not

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test for empty input list",
      "Input Data": "arr=[]",
      "Expected Output": "False"
    },
    {
      "Test Title": "Test for list with only one number",
      "Input Data": "arr=[3]",
      "Expected Output": "False"
    },
    {
      "Test Title": "Test for small input list with even product",
      "Input Data": "arr=[2, 4, 6]",
      "Expected Output": "True"
    },
    {
      "Test Title": "Test for small input list with odd product",
      "Input Data": "arr=[1, 3, 5]",
      "Expected Output": "False"
    },
    {
      "Test Title": "Test for large input list with even product",
      "Input Data": "arr=[2, 4, 6, 8, 10, 12]",
      "Expected Output": "True"
    },
    {
      "Test Title": "Test for large input list with odd product",
      "Input Data": "arr=[1, 3, 5, 7, 9, 11]",
      "Expected Output": "False"
    },
    {
      "Test Title": "Test for negative numbers in input list",
      "Input Data": "arr=[-1, -2, -3]",
      "Expected Output": "True"
    },
    {
      "Test Title": "Test for zero in input list",
      "Input Data": "arr=[0]",
      "Expected Output": "True"
    },
    {
      "Test Title": "Test for input list with both odd and even numbers",
      "Input Data": "arr=[1, 2, 3, 4, 5, 6]",
      "Expected Output": "True"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_product_even([1, 2, 3]), False)

if __name__ == '__main__':
    unittest.main()