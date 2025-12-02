def get_pairs_count(arr, sum):
    if not isinstance(arr, list) or not all(isinstance(i, (int, float)) for i in arr) or not isinstance(sum, (int, float)) or sum < 0:
        raise TypeError("Invalid input types. Input list must be a list of numbers and sum must be a positive number.")
    
    pairs_count = 0
    freq_map = {}
    
    for num in arr:
        complement = sum - num
        if complement in freq_map:
            pairs_count += freq_map[complement]
        freq_map[num] = freq_map.get(num, 0) + 1
    
    return pairs_count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Input List",
      "Input Data": "arr=[], sum=5",
      "Expected Output": "0"
    },
    {
      "Test Title": "Negative Numbers",
      "Input Data": "arr=[-1, 3, 4, -2, 1], sum=2",
      "Expected Output": "2"
    },
    {
      "Test Title": "Large Input List",
      "Input Data": "arr=[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], sum=1000",
      "Expected Output": "9"
    },
    {
      "Test Title": "Boundary Testing",
      "Input Data": "arr=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], sum=0",
      "Expected Output": "45"
    },
    {
      "Test Title": "Edge Case 1",
      "Input Data": "arr=[1, 1, 1, 1, 1, 1], sum=2",
      "Expected Output": "15"
    },
    {
      "Test Title": "Edge Case 2",
      "Input Data": "arr=[-1, -1, -1, -1, -1, -1], sum=-2",
      "Expected Output": "15"
    },
    {
      "Test Title": "Invalid Input Data",
      "Input Data": "arr=['a', 'b', 'c'], sum='d'",
      "Expected Output": "Invalid input data"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_get_pairs_count(self):
        self.assertEqual(get_pairs_count([1,1,1,1], 2), 6)

if __name__ == '__main__':
    unittest.main()