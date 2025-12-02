def move_zero(num_list):
    non_zero_elements = [x for x in num_list if x != 0]
    zero_elements = [x for x in num_list if x == 0]
    return non_zero_elements + zero_elements

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Move all zeroes to end of list with negative numbers",
      "Input Data": "num_list=[1,0,2,0,3,4,-1,-2,0]",
      "Expected Output": "[1,2,3,4,-1,-2,0,0,0]"
    },
    {
      "Test Title": "Mix of positive and negative numbers with zeroes",
      "Input Data": "num_list=[1,0,-2,0,3,4,-1,0,0]",
      "Expected Output": "[1,-2,3,4,-1,0,0,0,0]"
    },
    {
      "Test Title": "Large input list",
      "Input Data": "num_list=[0]*1000",
      "Expected Output": "[0,0,0,...,0,0,0]"
    },
    {
      "Test Title": "Move all zeroes to end of list with different numbers",
      "Input Data": "num_list=[7,0,5,0,3,4,0,2,0]",
      "Expected Output": "[7,5,3,4,2,0,0,0,0]"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_zero([1,0,2,0,3,4]), [1,2,3,4,0,0])

if __name__ == '__main__':
    unittest.main()