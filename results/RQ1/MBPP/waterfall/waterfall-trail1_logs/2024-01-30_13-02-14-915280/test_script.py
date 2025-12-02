def maximum(a, b):
    '''Write a python function to find the maximum of two numbers.'''
    if a == b:
        return a  # Return one of the equal numbers as the maximum
    return max(a, b)

# Test cases
assert maximum(5,10) == 10
assert maximum(8,8) == 8
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Maximum of two positive numbers",
      "Input Data": "parameter1=[1,2,3,1000000], parameter2='123'",
      "Expected Output": "1000000"
    },
    {
      "Test Title": "Maximum of two negative numbers",
      "Input Data": "parameter1=[-1,-2,-3,-1000000], parameter2='-123'",
      "Expected Output": "-1"
    },
    {
      "Test Title": "Maximum of equal numbers",
      "Input Data": "parameter1=[3,3,3000000], parameter2='3'",
      "Expected Output": "3"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum(5, 10), 10)

if __name__ == '__main__':
    unittest.main()