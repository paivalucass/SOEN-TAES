def max_element(l: list):
    if not isinstance(l, list) or len(l) == 0:
        return None

    max_num = float('-inf')
    for num in l:
        if isinstance(num, (int, float)):
            if num > max_num:
                max_num = num
    return max_num

# Test Cases:
{
  "requirement analysis": "Write test cases for max_element function",
  "test_cases": [
    {
      "Test Title": "Return maximum element in the list",
      "Input Data": "l=[1, 2, 3],l=[],l=[1]",
      "Expected Output": "3,None,1"
    },
    {
      "Test Title": "Return maximum element in the list",
      "Input Data": "l=[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],l=[],l=[5]",
      "Expected Output": "123,None,5"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

if __name__ == '__main__':
    unittest.main()