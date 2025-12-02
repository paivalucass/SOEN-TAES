def second_smallest(numbers):
    if len(numbers) < 2:
        raise ValueError("Error: List must contain at least two elements")

    unique_numbers = list(set(numbers))
    
    if len(unique_numbers) < 2:
        raise ValueError("Error: List must contain at least two unique elements")

    sorted_unique_numbers = sorted(unique_numbers)
    second_smallest_number = sorted_unique_numbers[1]
    
    return second_smallest_number

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty List",
      "Input Data": "parameter1=[]",
      "Expected Output": "Error: List must contain at least two elements"
    },
    {
      "Test Title": "Single Element List",
      "Input Data": "parameter1=[5]",
      "Expected Output": "Error: List must contain at least two unique elements"
    },
    {
      "Test Title": "Multiple Elements List",
      "Input Data": "parameter1=[1, 2, -8, -2, 0, -2]",
      "Expected Output": "-2"
    },
    {
      "Test Title": "Large Input List",
      "Input Data": "parameter1=[1000, 2000, -800, -200, 0, -2000]",
      "Expected Output": "-800"
    },
    {
      "Test Title": "List with Negative & Multiple Numbers",
      "Input Data": "parameter1=[-5, -3, -1, -6]",
      "Expected Output": "-5"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(second_smallest([1, 2, -8, -2, 0, -2]), -2)

if __name__ == '__main__':
    unittest.main()