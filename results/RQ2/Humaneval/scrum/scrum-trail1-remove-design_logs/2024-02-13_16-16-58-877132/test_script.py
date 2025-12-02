def by_length(arr):
    num_to_word = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    sorted_arr = sorted([num for num in arr if 1 <= num <= 9])
    reversed_arr = sorted_arr[::-1]
    result = [num_to_word[num] for num in reversed_arr]
    
    return result
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Array Test",
      "Input Data": "arr=[]",
      "Expected Output": "[]"
    },
    {
      "Test Title": "Array with Strange Numbers Test",
      "Input Data": "arr=[1, -1, 55]",
      "Expected Output": "['One']"
    },
    {
      "Test Title": "Array with Integers Outside Range Test",
      "Input Data": "arr=[10, 11, 12]",
      "Expected Output": "[]"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])
        self.assertEqual(by_length([]), [])
        self.assertEqual(by_length([1, -1, 55]), ["One"])

if __name__ == '__main__':
    unittest.main()