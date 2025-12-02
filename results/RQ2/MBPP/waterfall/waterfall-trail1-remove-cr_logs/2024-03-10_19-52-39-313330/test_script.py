def frequency_lists(list1):
    frequency_dict = {}
    for sublist in list1:
        if not isinstance(sublist, list):
            raise TypeError("Input list should contain only lists")
        for element in sublist:
            if not isinstance(element, int):
                raise ValueError("Non-integer elements in input list")
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1
    return frequency_dict

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input - Flattened List with Integers",
      "Input Data": "list1=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]",
      "Expected Output": "{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}"
    },
    {
      "Test Title": "Empty Input List",
      "Input Data": "list1=[]",
      "Expected Output": "{}"
    },
    {
      "Test Title": "Input with Non-Integer Elements",
      "Input Data": "list1=[[1, 'a', 3], ['b', 5, 6, 2], [7, 8, 9, 5]]",
      "Expected Output": "Error: Non-integer elements in input list"
    },
    {
      "Test Title": "Large Input List",
      "Input Data": "list1=[[1, 2, 3] * 1000]",
      "Expected Output": "<Expected Output to be determined based on performance metrics and benchmarks>"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]), {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1})

if __name__ == '__main__':
    unittest.main()