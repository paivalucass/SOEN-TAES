def count_no_of_ways(n, k):
    if n == 0 or k == 0:
        return 0
    if n == 1:
        return k
    
    same = k
    diff = k * (k - 1)
    total = same + diff
    
    for i in range(3, n + 1):
        same = diff
        diff = total * (k - 1)
        total = same + diff
    
    return total

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input with small number of posts and colors",
      "Input Data": "n=2, k=4",
      "Expected Output": "16"
    },
    {
      "Test Title": "Valid input with large number of posts and colors",
      "Input Data": "n=10, k=3",
      "Expected Output": "810"
    },
    {
      "Test Title": "Boundary case with minimum number of posts and colors",
      "Input Data": "n=1, k=1",
      "Expected Output": "1"
    },
    {
      "Test Title": "Boundary case with large number of posts and minimum colors",
      "Input Data": "n=100, k=1",
      "Expected Output": "100"
    },
    {
      "Test Title": "Boundary case with n equals to zero",
      "Input Data": "n=0, k=3",
      "Expected Output": "0"
    },
    {
      "Test Title": "Boundary case with k equals to zero",
      "Input Data": "n=5, k=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Boundary case with n as a very large number",
      "Input Data": "n=1000000, k=4",
      "Expected Output": "16000000"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_no_of_ways(2, 4), 16)

if __name__ == '__main__':
    unittest.main()