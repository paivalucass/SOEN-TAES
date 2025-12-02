def next_smallest_palindrome(num):
    num += 1
    while str(num) != str(num)[::-1]:
        num += 1
    return num

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Input is single digit number",
      "Input Data": "num=5",
      "Expected Output": "5"
    },
    {
      "Test Title": "Input is a two-digit number",
      "Input Data": "num=22",
      "Expected Output": "22"
    },
    {
      "Test Title": "Input is a large number",
      "Input Data": "num=12345",
      "Expected Output": "12321"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_smallest_palindrome(99), 101)

if __name__ == '__main__':
    unittest.main()