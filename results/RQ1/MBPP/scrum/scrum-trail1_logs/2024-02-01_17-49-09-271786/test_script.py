def max_sum_list(lists):
    if not isinstance(lists, list) or any(not isinstance(sub_list, list) for sub_list in lists):
        raise ValueError("Input 'lists' should be a list of lists")

    if not lists:
        return None  # Return None for empty input list

    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    max_sum_list = None  # Initialize max_sum_list to None

    for sub_list in lists:
        current_sum = sum(sub_list)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_list = sub_list

    return max_sum_list

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input - Regular Scenario",
      "Input Data": "lists=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]",
      "Expected Output": "[10, 11, 12]"
    },
    {
      "Test Title": "Valid Input - Single List Scenario",
      "Input Data": "lists=[[1,2,3]]",
      "Expected Output": "[1, 2, 3]"
    },
    {
      "Test Title": "Valid Input - Empty List Scenario",
      "Input Data": "lists=[]",
      "Expected Output": "None"
    },
    {
      "Test Title": "Invalid Input - Non-list Input",
      "Input Data": "lists='invalid_input'",
      "Expected Output": "ValueError"
    },
    {
      "Test Title": "Invalid Input - Non-list Sublist",
      "Input Data": "lists=[[1,2,3], 'invalid_sublist']",
      "Expected Output": "ValueError"
    },
    {
      "Test Title": "Boundary Test - Lowest Sum",
      "Input Data": "lists=[[0], [1,2,3], [4,5,6]]",
      "Expected Output": "[4, 5, 6]"
    },
    {
      "Test Title": "Boundary Test - Highest Sum",
      "Input Data": "lists=[[-1,-2,-3], [4,5,6], [10,11,12]]",
      "Expected Output": "[10, 11, 12]"
    },
    {
      "Test Title": "Negative Test - Empty Sublist",
      "Input Data": "lists=[[1,2,3], [], [4,5,6]]",
      "Expected Output": "[4, 5, 6]"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]), [10, 11, 12])

if __name__ == '__main__':
    unittest.main()