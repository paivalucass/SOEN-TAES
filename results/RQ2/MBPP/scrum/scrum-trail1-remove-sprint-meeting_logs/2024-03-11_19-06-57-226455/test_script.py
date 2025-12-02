def jacobsthal_num(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Using memoization to improve performance
    def memoize(func):
        memo = {}

        def helper(x):
            if x not in memo:
                memo[x] = func(x)
            return memo[x]

        return helper

    @memoize
    def jacobsthal(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return jacobsthal(n-1) + 2*jacobsthal(n-2)

    return jacobsthal(n)

# Testing the function with a large value of n
result = jacobsthal_num(1000) # This will test the efficiency and correctness of the function
print(result)
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input Test",
      "Input Data": "parameter1=5",
      "Expected Output": 11
    },
    {
      "Test Title": "Boundary Input Test",
      "Input Data": "parameter1=0",
      "Expected Output": 1
    },
    {
      "Test Title": "Invalid Input Test",
      "Input Data": "parameter1=-5",
      "Expected Output": "Error: Input should be a non-negative integer"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(jacobsthal_num(5), 11)

if __name__ == '__main__':
    unittest.main()