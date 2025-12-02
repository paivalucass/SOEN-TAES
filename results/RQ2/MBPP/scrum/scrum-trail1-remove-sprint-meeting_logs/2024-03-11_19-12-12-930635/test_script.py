def right_insertion(sorted_list, new_value):
    if not sorted_list:
        return 0
    for i in range(len(sorted_list)):
        if new_value <= sorted_list[i]:
            return i
    return len(sorted_list)

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty List",
      "Input Data": "sorted_list=[], new_value=3",
      "Expected Output": "0"
    },
    {
      "Test Title": "Insert at Beginning",
      "Input Data": "sorted_list=[1,2,4,5], new_value=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Insert at End",
      "Input Data": "sorted_list=[1,2,4,5], new_value=6",
      "Expected Output": "4"
    },
    {
      "Test Title": "Insert in Middle",
      "Input Data": "sorted_list=[1,2,4,5], new_value=3",
      "Expected Output": "2"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()