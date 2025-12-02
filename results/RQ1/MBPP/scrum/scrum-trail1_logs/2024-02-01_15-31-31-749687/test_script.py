def find_Parity(x):
    return x % 2 != 0
# Test Cases:
{
  "revised_test_cases": [
    {
      "Test Title": "Test for odd number",
      "Input Data": "parameter1=3, parameter2='123'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Test for even number",
      "Input Data": "parameter1=4, parameter2='123'",
      "Expected Output": "False"
    },
    {
      "Test Title": "Test for negative number",
      "Input Data": "parameter1=-5, parameter2='123'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Test for zero",
      "Input Data": "parameter1=0, parameter2='123'",
      "Expected Output": "False"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Parity(12), False)

if __name__ == '__main__':
    unittest.main()