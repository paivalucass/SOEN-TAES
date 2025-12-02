def find_Max_Num(arr):
    if len(arr) == 0:
        return "Error: Empty array"

    sorted_arr = sorted(arr, reverse=True)
    if all(i >= 0 for i in arr):
        return int("".join(map(str, sorted_arr)))
    else:
        positive_nums = [str(i) for i in sorted_arr if i >= 0]
        negative_nums = [str(i) for i in sorted_arr if i < 0]
        return int("".join(positive_nums) + "".join(negative_nums))
# Test Cases:
{
  "requirement analysis": "analysis",
  "test_cases": [
    {
      "Test Title": "Test with non-ascending order input",
      "Input Data": "arr=[1,2,3]",
      "Expected Output": "321"
    },
    {
      "Test Title": "Test with empty array",
      "Input Data": "arr=[]",
      "Expected Output": "Error: Empty array"
    },
    {
      "Test Title": "Test with array containing duplicate digits",
      "Input Data": "arr=[1,1,2,3]",
      "Expected Output": "3321"
    },
    {
      "Test Title": "Test with array containing negative numbers",
      "Input Data": "arr=[-1,2,3]",
      "Expected Output": "321"
    },
    {
      "Test Title": "Test with large arrays",
      "Input Data": "arr=[9,8,7,6,5,4,3,2,1]",
      "Expected Output": "987654321"
    },
    {
      "Test Title": "Test with arrays with all the same numbers",
      "Input Data": "arr=[111,111,111]",
      "Expected Output": "111111111"
    },
    {
      "Test Title": "Test with arrays with both positive and negative numbers",
      "Input Data": "arr=[-1,1,2,-2]",
      "Expected Output": "211-1-2"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1,2,3]), 321)

if __name__ == '__main__':
    unittest.main()