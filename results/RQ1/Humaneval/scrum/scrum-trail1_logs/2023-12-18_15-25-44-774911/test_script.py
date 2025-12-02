def prime_length(string):
    if string is None or len(string) < 2:
        return False
    for i in range(2, int(len(string) ** 0.5) + 1):
        if len(string) % i == 0:
            return False
    return True
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty String",
      "Input Data": "parameter1=''",
      "Expected Output": "False"
    },
    {
      "Test Title": "None Input",
      "Input Data": "parameter1=None",
      "Expected Output": "False"
    },
    {
      "Test Title": "Single Character String",
      "Input Data": "parameter1='a'",
      "Expected Output": "False"
    },
    {
      "Test Title": "Short String",
      "Input Data": "parameter1='ab'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Medium Length String",
      "Input Data": "parameter1='abcdefgh'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Long String",
      "Input Data": "parameter1='abcdefghijklmnopqrstuvwxyz'",
      "Expected Output": "True"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_length('Hello'), True)
        self.assertEqual(prime_length('abcdcba'), True)
        self.assertEqual(prime_length('kittens'), True)
        self.assertEqual(prime_length('orange'), False)

if __name__ == '__main__':
    unittest.main()