def multiple_to_single(L):
    if not all(isinstance(x, int) and x > 0 for x in L):
        raise ValueError("Input list should only contain positive integers")
    return int(''.join(map(str, L)))



# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Joining multiple positive integers into a single integer",
      "Input Data": "L=[11, 33, 50]",
      "Expected Output": "113350"
    },
    {
      "Test Title": "Joining an empty input list",
      "Input Data": "L=[]",
      "Expected Output": "Error: Empty input list"
    },
    {
      "Test Title": "Joining a single integer in the input list",
      "Input Data": "L=[5]",
      "Expected Output": "5"
    },
    {
      "Test Title": "Joining a large list of positive integers",
      "Input Data": "L=[100, 200, 300, 400, 500]",
      "Expected Output": "100200300400500"
    },
    {
      "Test Title": "Input validation: Non-integer in the input list",
      "Input Data": "L=[11, 'abc', 50]",
      "Expected Output": "Error: Non-integer element in the input list"
    },
    {
      "Test Title": "Edge case: Joining negative integers",
      "Input Data": "L=[-5, -10, -15]",
      "Expected Output": "-5-10-15"
    },
    {
      "Test Title": "Edge case: Joining zero",
      "Input Data": "L=[0]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Edge case: Joining the maximum allowed integer value",
      "Input Data": "L=[2147483647]",
      "Expected Output": "2147483647"
    },
    {
      "Test Title": "Performance testing: Large number of input elements",
      "Input Data": "L=[1, 2, 3, ..., 10000]",
      "Expected Output": "123...10000"
    },
    {
      "Test Title": "Specific error message: Non-integer element in the input list",
      "Input Data": "L=[11, 22.5, 33]",
      "Expected Output": "Error: Non-integer element '22.5' in the input list"
    },
    {
      "Test Title": "Specific error message: Invalid data type in the input list",
      "Input Data": "L=[11, 'xyz', 33]",
      "Expected Output": "Error: Invalid data type 'xyz' in the input list"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiple_to_single([11, 33, 50]), 113350)

if __name__ == '__main__':
    unittest.main()