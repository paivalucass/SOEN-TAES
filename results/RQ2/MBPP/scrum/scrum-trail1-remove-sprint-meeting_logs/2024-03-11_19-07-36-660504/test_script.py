def unique_sublists(list1):
    unique_dict = {}
    for sublist in list1:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in unique_dict:
            unique_dict[tuple_sublist] += 1
        else:
            unique_dict[tuple_sublist] = 1
    return unique_dict

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Testing with an empty input list",
      "Input Data": "list1=[]",
      "Expected Output": "{}"
    },
    {
      "Test Title": "Testing with a single element input list",
      "Input Data": "list1=[[1, 2, 3]]",
      "Expected Output": "{(1, 2, 3): 1}"
    },
    {
      "Test Title": "Testing with repeated sublists",
      "Input Data": "list1=[[1, 2, 3], [1, 2, 3], [1, 2, 3]]",
      "Expected Output": "{(1, 2, 3): 3}"
    },
    {
      "Test Title": "Testing with a mix of sublists",
      "Input Data": "list1=[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]",
      "Expected Output": "{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()