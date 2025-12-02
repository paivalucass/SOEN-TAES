def special_factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Invalid input. Input value must be a positive integer."
    
    if n == 0:
        return 1

    result = 1
    for i in range(1, n+1):
        result *= factorial(i)

    return result


def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input - positive integer",
      "Input Data": "parameter1=4",
      "Expected Output": "288"
    },
    {
      "Test Title": "Valid input - large positive integer",
      "Input Data": "parameter1=10",
      "Expected Output": "6652800"
    },
    {
      "Test Title": "Valid input - edge case - input value of 1",
      "Input Data": "parameter1=1",
      "Expected Output": "1"
    },
    {
      "Test Title": "Valid input - edge case - input value of 0",
      "Input Data": "parameter1=0",
      "Expected Output": "1"
    },
    {
      "Test Title": "Invalid input - negative integer",
      "Input Data": "parameter1=-3",
      "Expected Output": "Error: Invalid input. Input value must be a positive integer."
    },
    {
      "Test Title": "Boundary Test - Large Input",
      "Input Data": "parameter1=100",
      "Expected Output": "Large number result"
    },
    { 
      "Test Title": "Boundary Test - Non-integer input",
      "Input Data": "parameter1='abc'",
      "Expected Output": "Error: Invalid input. Input value must be a positive integer."
    },
    {
      "Test Title": "Boundary Test - Special Characters",
      "Input Data": "parameter1=@#%",
      "Expected Output": "Error: Invalid input. Input value must be a positive integer."
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(special_factorial(4), 288)

if __name__ == '__main__':
    unittest.main()