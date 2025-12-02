def odd_num_sum(n) :
    if n <= 0:
        return 0  

    odd_sum = 0  
    for i in range(1, 2*n, 2):  
        odd_sum += i**4

    return odd_sum

# Testing the function
assert odd_num_sum(2) == 82
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test with n=2",
      "Input Data": "n=2",
      "Expected Output": "82"
    },
    {
      "Test Title": "Test with n=5",
      "Input Data": "n=5",
      "Expected Output": "1330"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_num_sum(2), 82)

if __name__ == '__main__':
    unittest.main()