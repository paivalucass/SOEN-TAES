def even_odd_palindrome(n):
    even_count = count_palindromes(1, n, "even")
    odd_count = count_palindromes(1, n, "odd")
    return (even_count, odd_count)

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def count_palindromes(start, end, type):
    count = 0
    for i in range(start, end+1):
        if is_palindrome(i) and (i % 2 == 0 if type == "even" else i % 2 != 0):
            count += 1
    return count
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test for input 3",
      "Input Data": "parameter1=3",
      "Expected Output": "(1, 2)"
    },
    {
      "Test Title": "Test for input 12",
      "Input Data": "parameter1=12",
      "Expected Output": "(4, 6)"
    },
    {
      "Test Title": "Test for input 1",
      "Input Data": "parameter1=1",
      "Expected Output": "(0, 1)"
    },
    {
      "Test Title": "Test for input 1000",
      "Input Data": "parameter1=1000",
      "Expected Output": "(498, 500)"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))
        self.assertEqual(even_odd_palindrome(12), (4, 6))

if __name__ == '__main__':
    unittest.main()