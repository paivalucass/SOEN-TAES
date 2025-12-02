def get_pairs_count(arr, sum):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr) or not isinstance(sum, int):
        return "Invalid input data"

    pair_count = 0
    hash_map = {}

    for num in arr:
        complement = sum - num
        if complement in hash_map:
            pair_count += hash_map[complement]
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    return pair_count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty input array",
      "Input Data": "arr=[], sum=5",
      "Expected Output": "0"
    },
    {
      "Test Title": "Negative target sum",
      "Input Data": "arr=[1,2,3,4], sum=-10",
      "Expected Output": "0"
    },
    {
      "Test Title": "Various input array sizes",
      "Input Data": "arr=[1,2,3], sum=5",
      "Expected Output": "2"
    },
    {
      "Test Title": "Stress testing with large input arrays",
      "Input Data": "arr=[1000000,2000000,3000000,4000000], sum=5000000",
      "Expected Output": "4"
    },
    {
      "Test Title": "Input arrays with all negative numbers",
      "Input Data": "arr=[-1,-2,-3,-4], sum=-5",
      "Expected Output": "2"
    },
    {
      "Test Title": "Zero as the target sum",
      "Input Data": "arr=[0,0,0,0], sum=0",
      "Expected Output": "6"
    },
    {
      "Test Title": "Input arrays with duplicate numbers",
      "Input Data": "arr=[1,1,2,2,3,3], sum=4",
      "Expected Output": "6"
    },
    {
      "Test Title": "Input arrays with both positive and negative numbers",
      "Input Data": "arr=[-2,-1,1,2], sum=0",
      "Expected Output": "2"
    },
    {
      "Test Title": "Handling invalid input data",
      "Input Data": "arr=[1,'a',3,4], sum=5",
      "Expected Output": "Invalid input data"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_pairs_count([1,1,1,1], 2), 6)

if __name__ == '__main__':
    unittest.main()